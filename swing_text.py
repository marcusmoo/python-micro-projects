# Text Adventure
import time

offbeat_next = False
text_speed = 0.6

def swing(text, new_line = True):
    length = len(text)

    global offbeat_next

    
    for i in range(0, length):
        
        if text[i] == " ":
            print(" ", end = "")
        
        else:
            if offbeat_next == False:
                print(text[i].lower(), end = "")
                offbeat_next = True
                time.sleep(text_speed * (2/3))
            
            else:
                print(text[i].upper(), end = "")
                offbeat_next = False
                time.sleep(text_speed * (1/3))

            
    if new_line == True:
        print("")
        




swing("hello I am talking in swing")
