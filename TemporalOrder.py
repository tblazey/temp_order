import time
from os import path
import random

from psychopy import visual,core,event,gui,data

#Every object is square, so a boundry is just center plus 1/2 the length
def get_boundries(object):
	[x,y] = object.pos
	object_left = x - object.size[0]/2
	object_right = x + object.size[0]/2
	object_down = y - object.size[0]/2
	object_up = y + object.size[0]/2
	return x, y, object_left, object_right, object_down, object_up

#Setup window, and mouse
window = visual.Window([1440,900], allowGUI=True, units='pix')
mouse = event.Mouse(visible=True, win=window)

#Setup dialog box
info = {'Subject':'', 'Maze':'A or B', 'Experimenter':''}
infoDlg = gui.DlgFromDict(dictionary=info, title='Temporal Order', 
                                           order=['Subject','Experimenter','Maze'])

#While keep looping until user selects A/a or B/b as the maze type
while True:   
    if infoDlg.OK:   
        if (info['Maze'] == 'A' or info['Maze'] == 'a' or info['Maze'] == 'B' or 
            info['Maze'] == 'b'):                
            #If data file already exists, append. If not, create a new file
            output_file = info['Subject'] + '.txt'
            if path.exists('/Users/Tyler/Desktop/' + output_file) is True:
                output = open('/Users/Tyler/Desktop/' + output_file, 'a')
                output.write('\n')
            else:
                output = open('/Users/Tyler/Desktop/' + output_file, 'w')
                output.write('Subject: %s\n\n' %(info['Subject']))                    
            #Write data
            date = time.strftime("%m-%d-%Y", time.localtime())
            start_time = time.strftime("%H:%M:%S", time.localtime())            
            output.write('Date: %s\n' %(date))
            output.write('Maze: %s\n' %(info['Maze']))
            output.write('Experimentor: %s\n' %(info['Experimenter']))
            output.write('Start Time: %s\n' %(start_time))
            break
        else:
            infoDlg = gui.DlgFromDict(dictionary=info, title='Temporal Order')    
    else:
        core.quit()

#Display instructions and wait for key press to continue.
intro = visual.TextStim(window,text='Welcome to the awesome temporal order test.' +  
                                    'Your task is to place the objects in the order in which you saw them. ok?')
intro.draw()
window.flip()
event.waitKeys()

#The positions list must be in left/right order for the data file order to be correct
positions = [[-615,340], [-410,340], [-205,340], [0,340], [205,340], [410,340], [615,340],
                   [-615,135], [-410,135], [-205,135], [0,135], [205,135], [410,135], [615,135]]
random_order = random.sample(positions, len(positions))

#Object_dictionary -> Key:Object name + image filename root.
if ( info['Maze'] == 'A' or info['Maze'] == 'a' ):
    object_dictionary = {'Bench':[], 'Bookcase':[], 'Coat_Rack':[], 'Door':[], 'Lamp':[],
                                    'Long_Table':[], 'Mirror':[], 'Potted_Plant':[], 'Stool':[], 'Table':[],
                                    'Wooden_Chest':[], 'Cushion_Bench':[], 'Rug':[], 'White_Potted_Plant':[]}
else:
    object_dictionary = {'Computer_Desk':[], 'Dining_Chair':[], 'Entertainment_Center':[],
                                    'File_Cabinet':[], 'Lamp_B':[], 'Long_Table_B':[], 'Plant':[], 
                                    'Purple_Chair':[], 'Rug_B':[], 'Sink':[], 'Trash_Can':[],
                                    'Umbrella_Stand':[], 'Window':[], 'Fireplace':[]}

#Place each object in a random location
objects = []
for object, rand in zip(object_dictionary.keys(), random_order):
    #First value is coordinates, second is the order
    object_dictionary[str(object)] = [rand,positions.index(rand)]
    loop_object = visual.PatchStim(window,tex='/Users/Tyler/github/temp_order/images/' + 
                                                       str(object) + '_Neutral.jpg', size=200, depth=1,
                                                       name=str(object), pos=rand)
    objects.append(loop_object)
    loop_object.setAutoDraw(True)

#Border used for indicating which object is seleceted
border = visual.PatchStim(window, size=210, color='black')

#Box_list -> Key: Object name + image filename root. Value is coordinates
box_list = [('box_one', [-615,-135]), ('box_two', [-410,-135]), ('box_three', [-205,-135]), 
                 ('box_four', [0,-135]), ('box_five', [205,-135]), ('box_six', [410,-135]), 
                 ('box_seven', [615,-135]), ('box_eight', [-615,-340]), ('box_nine', [-410,-340]),
                 ('box_ten', [-205,-340]), ('box_eleven', [0,-340]), ('box_twelve', [205,-340]),
                 ('box_thirteen', [410,-340]), ('box_fourteen', [615,-340])]

#Place each box in the correct location. Also get the collision boundries.
boxes = [] 
box_boundries = []
for box in box_list:
    loop_box = visual.PatchStim(window, tex='/Users/Tyler/github/temp_order/images/' + 
                                                   str(box[0]) + '.jpg', size=200 ,pos=box[1])   
    boxes.append(loop_box)
    box_boundries.append(get_boundries(loop_box))
    loop_box.setAutoDraw(True)
    
#Main loop. Keep looping until a break signal is received. 
while True:
    window.flip()
    
    #Get object collision boundries
    object_boundries = []
    for object in objects:
        object_boundries.append(get_boundries(object))
    
    #Reset mouse status
    [mouse_x, mouse_y] = mouse.getPos()
    [mouse_left, mouse_right, mouse_middle] = mouse.getPressed()
   
   # 0 = Don't need to move box. 1 = Need to move box.
    move_to_box = 0
    
    #If left mouse button is pressed
    if (mouse_left == 1):
        for obj, bound in zip(objects, object_boundries):                   
            #Check to see if mouse was pressed within that object
            if ((mouse_x >= bound[2] and mouse_x <= bound[3]) and 
                (mouse_y >= bound[4] and mouse_y <= bound[5])):                          
                #If it was, turn the border on and redraw everything
                border.setPos(obj.pos)
                border.draw()
                window.flip()                     
               
               #Wait for user to unpress, then press mouse
                while mouse_left == 1:
                    [mouse_left, mouse_right, mouse_middle] = mouse.getPressed()
                    event.clearEvents()               
                while (mouse_left == 0): 
                    [mouse_left, mouse_right, mouse_middle] = mouse.getPressed()
                    [mouse_x,mouse_y] = mouse.getPos()
                    event.clearEvents()
                    
                    if (mouse_left == 1):
                        for box, box_bound in zip(boxes, box_boundries):
                            #If the mouse was pressed within that box
                            if ((mouse_x >= box_bound[2] and mouse_x <= box_bound[3]) and 
                                    (mouse_y >= box_bound[4] and mouse_y <= box_bound[5])):
                                for obj_check, bound_check in zip(objects, object_boundries):
                                    #If there already is an object in that box, move that 
                                    #(i.e. not selected) object back to it's start
                                    if (obj_check.pos[0] == box.pos[0] and 
                                            obj_check.pos[1] == box.pos[1] and 
                                            obj_check.name != obj.name):
                                        obj_check.setPos(object_dictionary[obj_check.name][0])
                                        #Don't check all the other objects
                                        break
                                move_to_box = 1
                                #Don't check all the other boxes
                                break
                        
                        #If necessary, move the object to the box. Otherwise move back to start.
                        if move_to_box == 1:
                            obj.setPos(box.pos)
                        else:
                            obj.setPos(object_dictionary[obj.name][0])
                        #Clear any events that occured while checking where the mouse was pressed.
                        event.clearEvents()
                
                #Wait for user to depress mouse before continuing. 
                while (mouse_left == 1):
                    [mouse_left, mouse_right, mouse_middle] = mouse.getPressed()
                    event.clearEvents()
                #Don't check all other boxes
                break 
    
    #Quit 
    if len(event.getKeys(keyList=['q'])) > 0:
        core.quit()
   
   #Go to confirm quit screen.
    if len(event.getKeys(keyList=['f'])) > 0:
        #List for the number of objects in their original places
        in_orig = []
        for object, box in zip(objects, boxes):
            box.setAutoDraw(False)
            object.setAutoDraw(False)
            #If the object is within its original starting location, add it to the in_orig list
            if (object.pos[0] == object_dictionary[object.name][0][0] and 
                    object.pos[1] == object_dictionary[object.name][0][1]):
                in_orig.append(object.name)
        #Show user some text, asking them if they really want to quit. Also show number of 
        #objects that have not been places
        confirm = visual.TextStim(window, text='There are ' + str(len(in_orig)) + 
                                                 ' left in their original places. Press f to quit or b to go back')
        confirm.draw()
        window.flip()
       
       #Loop until the user has made a choice to continue or to quit
        while True:
            #Quit
            if len(event.getKeys(keyList=['f'])) > 0:
                #List for the order user put the objects in 
                output_order = []
                for box in boxes:
                    #Whether or not a box has no object in it. 1=Yes 0 =No.
                    missing = 1
                    for obj in objects:
                        #Check to see if object and box have the same postion. 
                        if ( obj.pos[0] == box.pos[0] and obj.pos[1] == box.pos[1] ):
                            output_order.append(str(obj.name))
                            missing = 0
                            #Don't check all the remaining objets
                            break
                    #If no object was in that box, report it.
                    if missing == 1:
                        output_order.append( 'None' )
                
                #Get and write the end time
                end_time = time.strftime("%H:%M:%S", time.localtime())
                output.write('End Time: %s\n' %(end_time))
                #Sort the object dictionary by the presented order
                sorted_objects = sorted(object_dictionary.items(), key=lambda x: x[1][1])
                #Print the key's of the sorted list
                output.write('Random Order: ' + str([ sorted_objects[i][0] for i in range(len(sorted_objects)) ]) + '\n')
                output.write('Subject Order: ' + str(output_order) + '\n')
                #If there are any unordered objects, write them
                if len(in_orig) > 0:
                    output.write('Unordered Objects: ' + str(in_orig) + '\n')
                #And quit!
                core.quit()
            
            #If user pressed b, go back into the program
            if len(event.getKeys(keyList=['b'])) > 0:
                for object, box in zip(objects, boxes):
                    box.setAutoDraw(True)
                    object.setAutoDraw(True)
                break
                