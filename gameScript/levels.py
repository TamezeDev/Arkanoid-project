import pygame
from .system import box_position, box_dimension, box_list, box_colors, width, white, gray_borders,green, red, blue, yellow, screen

def create_level(level):
    """Function to get the corners of each box. Very important to create all levels

Returns:
list: list of lists with the positions of the boxes
    """
    if level == 1:
        for i in range(0,5):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22  
    box_position[0] = 22
    box_position[1] = 80 

    if level == 2:
        for i in range(0,5):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 124
            box_position[1] += 22  
            box_position[0] = 22  
    box_position[0] = 22
    box_position[1] = 80 
    
    if level == 3:
        change_position = [22,84,22,84,22]
        for i in range(0,5):
            box_position[0] = change_position[i]
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 124
            box_position[1] += 22  
    box_position[0] = 22
    box_position[1] = 80 
    if level == 4:
        change_position = [22,84,84,84,22]
        for i in range(0,5):
            box_position[0] = change_position[i]
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                if change_position[i] == 22:
                    box_position[0] += 62
                else:
                    box_position[0] += 124
            box_position[1] += 22  
    box_position[0] = 22
    box_position[1] = 80 

    if level == 5:
        for i in range(0,6):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22  
    box_position[0] = 22
    box_position[1] = 80 
    if level == 6:
        for i in range(0,6):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22  
        for element in box_list:
            if box_list.index(element)!= 0 and box_list.index(element) % 3 == 0:
                box_list.remove(element)
    box_position[0] = 22
    box_position[1] = 80 

    if level == 7:
        box_colors.append(gray_borders)
        box_colors.append(white)
        for i in range(0,8):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22  
        for element in box_list[4::4]:
            box_list.remove(element)
        box_list.remove(box_list[0])
    box_position[0] = 22
    box_position[1] = 80 

    if level == 8:
        box_colors.append(green)
        box_colors.append(blue)
        for i in range(0,8):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22  
        for element in box_list:
            if box_list.index(element) % 2 == 0:
                box_list.remove(element)
    box_position[0] = 22
    box_position[1] = 80 
    if level == 9:
        change_position = [22,32,22,32,22,32,22,32,22,32]
        for i in range(0,10):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = change_position[i]  
    box_position[0] = 22
    box_position[1] = 80 
    if level == 10:
        change_position = [84,22,84,22,84,22,84,22,84,22]
        for i in range(0,10):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 124
            box_position[1] += 22  
            box_position[0] = change_position[i]
    box_position[0] = 22
    box_position[1] = 80 

    if level == 11:
        box_colors.append(yellow)
        box_colors.append(red)
        for i in range(0,12):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 124
            box_position[1] += 22  
            box_position[0] = 22
    box_position[0] = 22
    box_position[1] = 80 

    if level == 12:
        for i in range(0,12):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22
        for element in box_list:
            if 200 < element[0] < width - 200 and  125 < element[1] < 277:
                box_list.remove(element)
    box_position[0] = 22
    box_position[1] = 80 

    if level == 13:
        for i in range(0,12):
            while box_position[0] < width -22:
                box_list.extend([[box_position[0],box_position[1],box_dimension[0],box_dimension[1]]])
                box_position[0] += 62
            box_position[1] += 22  
            box_position[0] = 22
    box_position[0] = 22
    box_position[1] = 80 

          
def draw_boxes_level(level):
    """Function that draws the level boxes"""
    if 1 <= level  <= 13:
        for position in box_list:
            if position[1] == 80:
                pygame.draw.rect(screen,box_colors[0],position)
            elif position[1] == 102:
                pygame.draw.rect(screen,box_colors[1],position)
            elif position[1] == 124:
                pygame.draw.rect(screen,box_colors[2],position)
            elif position[1] == 146:
                pygame.draw.rect(screen,box_colors[3],position)
            elif position[1] == 168:
                pygame.draw.rect(screen,box_colors[4],position)
            elif position[1] == 190:
                pygame.draw.rect(screen,box_colors[5],position)
            elif position[1] == 212:
                pygame.draw.rect(screen,box_colors[6],position)  
            elif position[1] == 234:
                pygame.draw.rect(screen,box_colors[7],position)  
            elif position[1] == 256:
                pygame.draw.rect(screen,box_colors[8],position)
            elif position[1] == 278:
                pygame.draw.rect(screen,box_colors[9],position)  
            elif position[1] == 300:
                pygame.draw.rect(screen,box_colors[10],position)
            elif position[1] == 322:
                pygame.draw.rect(screen,box_colors[11],position)      