import pygame
import time
import json
from .system import screen, white, black, stick_color

#Start of the font module
pygame.font.init()

### Defining the variables ###
brown = (157,63,41)
logo_color = (0,66,198)

#Parent class of side elements
class Side_elements:
    def __init__(self,name, color, position):
        self.name = name
        self.color = color
        self.position = position

#Logo - Arkanoid
logo = Side_elements("ARKANOID",logo_color,(1120, 80))      
#Score-logo
score_logo = Side_elements("SCORE", brown , (1115, 160))
#High-score-logo
high_score_logo = Side_elements("HIGH SCORE", brown, (1120, 300))
#Game score (current)
score_nums = Side_elements(0, white, (1115, 200))
#Hicg-score
high_score_nums = Side_elements(0,white, (1115, 340))

#Current Level
level = 1 #starter level
final_level = 13 #last level
level_logo = Side_elements('Level',brown, (1115, 450)) #Logo-level
current_level = Side_elements(level ,white, (1115, 490)) #Current-level

#Init Level
current_level_init = Side_elements(f'Level: {level}',white, (600, 384))

#Current lives
lives = 2 #starter lives
lives_logo = Side_elements('Lives: ' ,brown, (1115, 600)) 
current_lives = Side_elements(lives ,white, (1160, 600))

def start_game():
    """Game start function
    """
    title = Side_elements('Arcanoid', logo_color, (600, 160))
    subtitle = Side_elements('Press Enter to start the game', white, (600,300))
    reset_score = Side_elements('Press R to reset high score', white, (600,420))
    copyright = Side_elements('Developed  by ZeKiT@M', white, (600,650))
    screen.fill(black)
    show_sidebar_items('./fonts/Arka_solid.ttf',title,120)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',subtitle,40)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',reset_score,25)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',copyright,25)
    pygame.display.flip()

def show_init_level(get_lives):
    """Function that shows the pre-level
    """
    global lives
    lives = get_lives
    current_lives.name = lives
    screen.fill(black)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',current_level_init,40)
    pygame.display.flip()
    time.sleep(2)

def clear_level(get_level):
    """Function to indicate that the level is completed
    Args:
    get_level (int): Receives the level you have completed
    """
    clear_level = Side_elements('Clear level', white, (530,400))
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',clear_level,30)
    global level
    level = get_level
    current_level.name = level
    current_level_init.name = f'Level: {level}'
    pygame.display.flip()
    time.sleep(2)

def show_status_game(str, size):
    """Function to show the status of the game (win or lose) and the final score
    """
    screen.fill(black)
    string = Side_elements(str, white, (600,200))
    your_score = Side_elements(f'Your score:  {score_nums.name}', white, (600,365))
    high_score = Side_elements(f'High score:  {high_score_nums.name}', white, (600, 500))
    show_sidebar_items('./fonts/Arka_solid.ttf',string,size)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',your_score,40)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',high_score,40)
    pygame.display.flip()
    time.sleep(4)
    score_nums.name = 0
    global level
    level = 1
    current_level_init.name = f'Level:  {level}'
    current_level.name = level
    if high_score_nums.name  > data:
        save_high_score(high_score_nums.name)

def draw_sticks_lives(live):
    """Function to draw life bats in the sidebar

    Args:
        live (int): left lives (current live doesn't count)
    """
    sticks_position = ([1070, 630],[1070,660],[1070,690])
    for i in range(live):
        pygame.draw.rect(screen,stick_color, [sticks_position[i][0], sticks_position[i][1], 100,15])

def draw_reset_highScore_message():
    reset_score = Side_elements('High score erased', white, (600,470))
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',reset_score,25)
    pygame.display.flip()

def show_sidebar_items(font, element,size):
    """Function to paint the sidebar elements"""
    font_logo = pygame.font.Font(font, size)
    save_data_text = font_logo.render(str(element.name), True, element.color)
    rect_text = save_data_text.get_rect(center=(element.position[0],element.position[1]))
    screen.blit(save_data_text,rect_text)

def update_sidebar():
    """Function that updates the sidebar
    """    
    show_sidebar_items('./fonts/Arka_solid.ttf',logo,25)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',score_logo,25)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',high_score_logo,24)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',score_nums,24)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',high_score_nums,24)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',level_logo,25)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',lives_logo,25)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',current_lives,24)
    show_sidebar_items('./fonts/PaytoneOne-Regular.ttf',current_level,24)
    draw_sticks_lives(lives)

def load_score():
    """Function to load the top score data
    """
    global high_score_nums
    with open('./high_score.json', 'r') as f:
        global data
        data = json.load(f)
        high_score_nums.name = data

def save_high_score(score):
    """Function to save the highest score or reset high-score to 0
    """
    with open('./high_score.json', 'w') as f:
        json.dump(score, f)