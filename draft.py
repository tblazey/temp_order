from psychopy import visual,core,event,gui,data
import time
from os import path
#from numpy import *
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


info = {'Subject':'','Maze':'A or B','Experimentor':''}
infoDlg = gui.DlgFromDict(dictionary=info, title='Temporal Order')
while True:
    if infoDlg.OK:
        if info['Maze']=='A' or info['Maze']=='a' or info['Maze']=='B' or info['Maze']=='b':
            output_file = info['Subject']+'.txt'
            if path.exists('/Users/Tyler/Desktop/'+output_file) is True:
                output = open('/Users/Tyler/Desktop/'+output_file,'a')
                output.write('\n')
            else:
                output = open('/Users/Tyler/Desktop/'+output_file,'w')
                output.write( 'Subject: %s\n' %(info['Subject']) )
            date = time.strftime("%m-%d-%Y",time.localtime())
            start_time = time.strftime("%H:%M:%S",time.localtime())
            output.write( 'Date: %s\n' %(date) )
            output.write( 'Start Time: %s\n' %(start_time))
            output.write( 'Maze: %s\n' %(info['Maze']) )
            output.write( 'Experimentor: %s\n' %(info['Experimentor']) )
            break
        else:
            infoDlg = gui.DlgFromDict(dictionary=info, title='Temporal Order')
    else:
        core.quit()

#Setup the positions list and then get one in a random order. Positions list has to be in order to output of the orignal order to work...
positions = [ [-615,340], [-410,340], [-205,340], [0,340]]#, [205,340], [410,340], [615,340],[-615,135], [-410,135], [-205,135], [0,135], [205,135], [410,135], [615,135] ]
random_order = random.sample(positions,len(positions))

if info['Maze'] == 'A' or info['Maze'] == 'a':
    #setup the objects
    object_one = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Bench_Neutral.jpg",size=200,depth=1,name='Bench')
    object_two = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Bookcase_Neutral.jpg",size=200,depth=1,name='Bookcase')
    object_three = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Coat_Rack_Neutral.jpg",size=200,depth=1,name='CoatRack')
    object_four = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Door_Neutral.jpg",size=200,depth=1,name='Door')
else:
    object_one = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Bench_Neutral.jpg",size=200,depth=1,name='object_one')
    object_two = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Bookcase_Neutral.jpg",size=200,depth=1,name='object_two')
    object_three = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Coat_Rack_Neutral.jpg",size=200,depth=1,name='object_three')
    object_four = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Door_Neutral.jpg",size=200,depth=1,name='object_four')
#object_five = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Lamp_Neutral.jpg",size=200,depth=1,name='object_five')
#object_six = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Long_Table_Neutral.jpg",size=200,depth=1,name='object_six')
#object_seven = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Mirror_Neutral.jpg",size=200,depth=1,name='object_seven')
#object_eight = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Potted_Plant_Neutral.jpg",depth=1,size=200,name='object_eight')
#object_nine = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Stool_Neutral.jpg",size=200,depth=1,name='object_nine')
#object_ten = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Table_Neutral.jpg",size=200,depth=1,name='object_ten')
#object_eleven = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Wooden_Chest_Neutral.jpg",depth=1,size=200,name='object_eleven')
#object_twelve = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Cushion_Bench_Neutral.jpg",depth=1,size=200,name='object_twelve')
#object_thirteen = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/Rug_Neutral.jpg",size=200,depth=1,name='object_thirteen')
#object_fourteen = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/White_Potted_Plant_Neutral.jpg",depth=1,size=200,name='object_fourteen')

#setup boder
border = visual.PatchStim(window,size=210,color='black')

#setup the boxes
box_one = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_one.jpg",size=200,name='box_one')
box_two = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_two.jpg",size=200,name='box_one')
box_three = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_three.jpg",size=200,name='box_three')
box_four = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_four.jpg",size=200,name='box_four')
#box_five = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_five.jpg",size=200,name='box_five')
#box_six = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_six.jpg",size=200,name='box_six')
#box_seven = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_seven.jpg",size=200,name='box_seven')
#box_eight = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_eight.jpg",size=200,name='box_eight')
#box_nine = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_nine.jpg",size=200,name='box_nine')
#box_ten = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_ten.jpg",size=200,name='box_ten')
#box_eleven = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_eleven.jpg",size=200,name='box_eleven')
#box_twelve = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_twelve.jpg",size=200,name='box_twelve')
#box_thirteen = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_thirteen.jpg",size=200,name='box_thirteen')
#box_fourteen = visual.PatchStim(window,tex="/Users/Tyler/github/temp_order/images/box_fourteen.jpg",size=200,name='box_fourteen')

intro = visual.TextStim(window,text='Welcome to the awesome temporal order test. Your task is to place the objects in the order in which you saw them. ok?')
intro.draw()
window.flip()
event.waitKeys()

#setup object list, then use it randomly select a start location. Record the start location a dictionary for later use
objects = ( object_one, object_two, object_three, object_four)#, object_five, object_six, object_seven,object_eight,object_nine,object_ten,object_eleven,object_twelve,object_thirteen,object_fourteen )
start_dictionary = {}; order_dictionary = {}
for object,rand in zip(objects,random_order):
    object.setPos(rand)
    start_dictionary[object.name] = rand
    order_dictionary[positions.index(rand)] = object.name
    object.setAutoDraw(True)

#setup lists for the boxes and for the boundries of the boxes
boxes = ( box_one,box_two,box_three,box_four)#,box_five,box_six,box_seven,box_eight,box_nine,box_ten,box_eleven,box_twelve,box_thirteen,box_fourteen )
box_positions = [ [-615,-135], [-410,-135], [-205,-135], [0,-135]]#, [205,-135], [410,-135], [615,-135], [-615,-340], [-410,-340], [-205,-340], [0,-340], [205,-340], [410,-340], [615,-340] ]
box_boundries = []
for box,pos in zip(boxes,box_positions):
    box.setPos(pos)
    boundry = get_boundries(box)
    box_boundries.append(boundry)
    box.setAutoDraw(True)

while True:
    
    #draw the stimuli
    window.flip()
    
    #setup object boundries and make an object boundry list
    object_boundries = []
    for object in objects:
        boundry = get_boundries(object)
        object_boundries.append(boundry)
    
    #get mouse position and pressed status
    [mouse_x,mouse_y] = mouse.getPos()
    [mouse_left,mouse_right,mouse_middle] = mouse.getPressed()
    
    move_to_box = 0
    if ( mouse_left == 1):
        #loop through all the objects
        for obj,bound in zip(objects,object_boundries):
            #check to see if mouse was pressed within that object
            if ( (mouse_x >= bound[2] and mouse_x <= bound[3]) and (mouse_y >= bound[4] and mouse_y <= bound[5])): 
                #if it was, turn the border on and redraw everything
                border.setPos(obj.pos)
                obj.draw()
                border.draw()
                window.flip()
                #wait for user to unclick mouse before continuing
                while mouse_left == 1:
                    [mouse_left,mouse_right,mouse_middle] = mouse.getPressed()
                    event.clearEvents()
                #wait for user to click mouse 
                while (mouse_left == 0): 
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
                                        obj_check.setPos(start_dictionary[obj_check.name])
                                        break #don't check all the other objects
                                move_to_box = 1
                                break # don't check all the boxes
                        if move_to_box == 1:
                            obj.setPos(box.pos)
                        #if user clicked, but not in box, move it back to the start
                        else:
                            obj.setPos(start_dictionary[obj.name])
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
            if (object.pos[0] == start_dictionary[object.name][0]  and object.pos[1] == start_dictionary[object.name][1] ):
                in_orig.append(object.name)
        confirm = visual.TextStim(window,text='There are ' + str(len(in_orig)) + ' left in their original places. Press f to quit or b to go back')
        confirm.draw()
        window.flip()
        while True:
            if len(event.getKeys(keyList=['f'])) > 0:
                output_order = {}
                count = 1
                for box in boxes:
                    missing = 1
                    for obj in objects:
                        if ( obj.pos[0] == box.pos[0] and obj.pos[1] == box.pos[1] ):
                            output_order[count] = str(obj.name)
                            missing = 0
                            break
                    if missing == 1:
                        output_order[count] = 'none'
                    count += 1
                end_time = time.strftime("%H:%M:%S",time.localtime())
                output.write( 'End Time: %s\n' %(end_time))
                output.write('Random Order: ' + str(order_dictionary.values()) + '\n')
                output.write('Subject Order: ' + str(output_order.values()) + '\n')
                output.write('Unordered Objects: ' + str(in_orig) + '\n')
                core.quit()
            if len(event.getKeys(keyList=['b'])) > 0:
                for object,box in zip(objects,boxes):
                    box.setAutoDraw(True)
                    object.setAutoDraw(True)
                break
                