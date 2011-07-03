from psychopy import visual,core,event,gui,data
import time
from os import path
import random

#function to get the 'collision boundries'
def get_boundries(object):
	[x,y] = object.pos
	object_left = x - object.size[0]/2
	object_right = x + object.size[0]/2
	object_down = y - object.size[0]/2
	object_up = y + object.size[0]/2
	return x,y,object_left,object_right,object_down,object_up

#Setup Window and mouse
window = visual.Window([1440,900],allowGUI=True, units='pix',)
mouse = event.Mouse(visible=True,win=window)

#Setup dictionary and dialog box
info = {'Subject':'','Maze':'A or B','Experimenter':''}
infoDlg = gui.DlgFromDict(dictionary=info, title='Temporal Order',order=['Subject','Experimenter','Maze'])

#Loop until user has entered either A or B 
while True:
    if infoDlg.OK:
        #If user has entered A or B, go on
        if info['Maze']=='A' or info['Maze']=='a' or info['Maze']=='B' or info['Maze']=='b':
            output_file = info['Subject']+'.txt'
           #Check if a output file exits. If it does append, if not create a new file
            if path.exists('/Users/Tyler/Desktop/'+output_file) is True:
                output = open('/Users/Tyler/Desktop/'+output_file,'a')
                output.write('\n')
            else:
                output = open('/Users/Tyler/Desktop/'+output_file,'w')
                output.write( 'Subject: %s\n\n' %(info['Subject']) )
           #Get date and time
            date = time.strftime("%m-%d-%Y",time.localtime())
            start_time = time.strftime("%H:%M:%S",time.localtime())
            #Write out data to file
            output.write( 'Date: %s\n' %(date) )
            output.write( 'Start Time: %s\n' %(start_time))
            output.write( 'Maze: %s\n' %(info['Maze']) )
            output.write( 'Experimentor: %s\n' %(info['Experimenter']) )
            break
        #If user has not entered A or B, keep looping
        else:
            infoDlg = gui.DlgFromDict(dictionary=info, title='Temporal Order')
    #If user has selected cancel, quit 
    else:
        core.quit()

#Show user instructions
intro = visual.TextStim(window,text='Welcome to the awesome temporal order test. Your task is to place the objects in the order in which you saw them. ok?')
intro.draw()
window.flip()

#Wait for user to press key before continuing
event.waitKeys()

#Setup the postions list. Note, that they output file will not produce the correct staring order if this list is not in order. 
positions = [ [-615,340], [-410,340], [-205,340], [0,340]]
#Get random order
random_order = random.sample(positions,len(positions))

#Create object dictionary: Key is object name (used for getting image filename). First value will be the start coordinates, second value will be the presentation order.
object_dictionary = { 'Bench':[],'Bookcase':[],'Coat_Rack':[],'Door':[] }
#Create object list
objects = []

#Loop through all the items in the object dictionary and the random order
for object,rand in zip(object_dictionary.keys(),random_order):
    #add the coordinates and starting position into dictionary
    object_dictionary[str(object)] = [rand,positions.index(rand)]
    #Set up object, placing it in a random location
    loop_object = visual.PatchStim(window,tex='/Users/Tyler/github/temp_order/images/'+str(object)+'_Neutral.jpg',size=200,depth=1,name=str(object),pos=rand)
    #add object to objects and turn on autodraw
    objects.append(loop_object)
    loop_object.setAutoDraw(True)

#Setup the border. Used for indicating which picture is selected
border = visual.PatchStim(window,size=210,color='black')

#Setup box list: First value is the box name (used for getting image), and the second is the box coordinates
box_list = [ ('box_one',[-615,-135]), ('box_two',[-410,-135]), ('box_three',[-205,-135]), ('box_four',[0,-135]) ]
#Setup lists for the boxes and for there boundries
boxes = [] 
box_boundries = []
for box in box_list:
   #Setup box in correct location
    loop_box = visual.PatchStim(window,tex='/Users/Tyler/github/temp_order/images/'+str(box[0])+'.jpg',size=200,pos=box[1])
    #Add box to boxes, get the boundries, and turn on autodraw
    boxes.append(loop_box)
    box_boundries.append(get_boundries(loop_box))
    loop_box.setAutoDraw(True)

while True:
    
    #draw the stimuli
    window.flip()
    
    #Add the boundries for every single object to a list
    object_boundries = []
    for object in objects:
        object_boundries.append(get_boundries(object))
    
    #get mouse position and pressed status
    [mouse_x,mouse_y] = mouse.getPos()
    [mouse_left,mouse_right,mouse_middle] = mouse.getPressed()
    
    #set a varible to indicate whether we need to move an objet to box. 0 = No. 1 = Yes.
    move_to_box = 0
    
    #If user preseted the left mouse button...
    if ( mouse_left == 1):
        #Loop through all the objects
        for obj,bound in zip(objects,object_boundries):
            #Check to see if mouse was pressed within that object
            if ( (mouse_x >= bound[2] and mouse_x <= bound[3]) and (mouse_y >= bound[4] and mouse_y <= bound[5])): 
                #If it was, turn the border on and redraw everything
                border.setPos(obj.pos)
                border.draw()
                window.flip()
                #Wait for user to unclick mouse before continuing
                while mouse_left == 1:
                    [mouse_left,mouse_right,mouse_middle] = mouse.getPressed()
                    event.clearEvents()
                #Wait for user to click mouse 
                while (mouse_left == 0): 
                    #refresh the mouse events
                    [mouse_left,mouse_right,mouse_middle] = mouse.getPressed()
                    [mouse_x,mouse_y] = mouse.getPos()
                    if (mouse_left == 1):
                        #loop through all the boxes
                        for box,box_bound in zip(boxes,box_boundries):
                            if ( (mouse_x >= box_bound[2] and mouse_x <= box_bound[3]) and (mouse_y >= box_bound[4] and mouse_y <= box_bound[5]) ):
                                #loop, again, through all the objects
                                for obj_check,bound_check in zip(objects,object_boundries):
                                    #if there is an object in that box, move it back to the start
                                    if ( obj_check.pos[0] == box.pos[0] and obj_check.pos[1] == box.pos[1] and obj_check.name != obj.name ):
                                        obj_check.setPos(object_dictionary[obj_check.name][0])
                                        break #don't check all the other objects
                                move_to_box = 1
                                break # don't check all the boxes
                        if move_to_box == 1:
                            obj.setPos(box.pos)
                        #if user clicked, but not in box, move it back to the start
                        else:
                            obj.setPos(object_dictionary[obj.name][0])
                    event.clearEvents()
                #wait for user to depress mouse before continuing. 
                while (mouse_left == 1):
                    [mouse_left,mouse_right,mouse_middle] = mouse.getPressed()
                    event.clearEvents()
                break #don't check out all the objects
    if len(event.getKeys(keyList=['q'])) > 0:
        core.quit()
    if len(event.getKeys(keyList=['f'])) > 0:
        in_orig = []
        for object,box in zip(objects,boxes):
            box.setAutoDraw(False)
            object.setAutoDraw(False)
            if (object.pos[0] == object_dictionary[obj_check.name][0][0]  and object.pos[1] == object_dictionary[obj_check.name][0][1]  ):
                in_orig.append(object.name)
        confirm = visual.TextStim(window,text='There are ' + str(len(in_orig)) + ' left in their original places. Press f to quit or b to go back')
        confirm.draw()
        window.flip()
        while True:
            if len(event.getKeys(keyList=['f'])) > 0:
                output_order = []
                for box in boxes:
                    missing = 1
                    for obj in objects:
                        if ( obj.pos[0] == box.pos[0] and obj.pos[1] == box.pos[1] ):
                            output_order.append( str(obj.name) )
                            missing = 0
                            break
                    if missing == 1:
                        output_order.append( 'None' )
                end_time = time.strftime("%H:%M:%S",time.localtime())
                output.write( 'End Time: %s\n' %(end_time))
                sorted_objects = sorted(object_dictionary.items(), key=lambda x: x[1][1])
                output.write('Random Order: ' + str([ sorted_objects[i][0] for i in range(len(sorted_objects)) ]) + '\n')
                output.write('Subject Order: ' + str(output_order) + '\n')
                output.write('Unordered Objects: ' + str(in_orig) + '\n')
                core.quit()
            if len(event.getKeys(keyList=['b'])) > 0:
                for object,box in zip(objects,boxes):
                    box.setAutoDraw(True)
                    object.setAutoDraw(True)
                break
                