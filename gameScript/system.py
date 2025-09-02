import pygame
import random
import time

#Strating Audio module
pygame.mixer.init()

####Variable declaration######

#Game screen parameters
width = 1030 #Width
height = 768 #Height

#Window parameters
width_screen = 1200 #Width
height_screen = 768 #Height
size = width_screen, height_screen  #resolution(width, height)

#Main colors
white = (255,255,255)
black = (0,0,0)
gray_borders = (64,64,64)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,32,96)
green = (0,176,80)
background_level = [(255,178,125),(199,133,200),(8,100,139),(107,208,137),(96,72,120),(119,23,34),(57,45,13)] #Random background colors of stages

#Bat Parameters
stick_color = ((30,134,255)) #Bat color Blue
stick_position = [500,700,120,20]  #Bat position(x,y,long,gross)
stick_small = 60
stick_large = 180
stick_move = [3,3] #sense of bat movement (implies speed)

#Boxes Parameters
box_dimension = [60,20] #Box dimensions (width, height)
box_position = [22,80] #Position of the first box (x,y)
box_colors = [red,yellow,blue,green,white,gray_borders] #initial box colors
box_list = [] #list of box positions (x,y,long,gross)

#Ball parameters2
ball_position = [width/2, 350 ,8] #position of the ball (x,y)
ball_direction = [5,5]      #direction of the ball (involves speed)
ball_on_air = True #Status about ball on air
ball_sticky = False #Status about the stick ball

#Items Parameters
pill_dimension = 8  #Ball radius
pill_position = []  #Items postion (x,y)
pill_colors = [red,yellow,blue,green,white,gray_borders] #Items colors
pill_random_color = 0  #Random color item fall

#Extra life
extra_live = False #Status about extra live

#Status temps
timer_event_reset_highScore = pygame.USEREVENT +1 #timer control for highScore events
timer_event_stick = pygame.USEREVENT +1 #timer control for bat events
timer_event_ball = pygame.USEREVENT +1 #timer control for ball events
timer_event_adhere_ball = pygame.USEREVENT +1 #timer control for stick ball events
timer_duration = 0  #time event
timer_status_stick_modified = False #Status about modified stick
timer_status_ball_modified = False #Status about modified speed-ball
timer_status_adhere_ball = False #Status about stick-ball

#Audio
start_game_sound = pygame.mixer.Sound("./sounds/start_game.mp3")
tracks_game = [pygame.mixer.Sound("./sounds/track_1.mp3"),pygame.mixer.Sound("./sounds/track_2.mp3"),pygame.mixer.Sound("./sounds/track_3.mp3"),pygame.mixer.Sound("./sounds/track_4.mp3"),pygame.mixer.Sound("./sounds/track_5.mp3")]
sound_stick = [pygame.mixer.Sound("./sounds/Arkanoid SFX (6).wav"),pygame.mixer.Sound("./sounds/Arkanoid SFX (7).wav"),pygame.mixer.Sound("./sounds/Arkanoid SFX (3).wav"), pygame.mixer.Sound("./sounds/Arkanoid SFX (4).wav")]
sound_walls = [pygame.mixer.Sound("./sounds/Arkanoid SFX (1).wav"),pygame.mixer.Sound("./sounds/Arkanoid SFX (2).wav")]
sound_blocks = pygame.mixer.Sound("./sounds/Arkanoid SFX (8).wav")
sound_fail = pygame.mixer.Sound("./sounds/Arkanoid SFX (10).wav")
sound_clear_level = pygame.mixer.Sound("./sounds/Arkanoid SFX (9).wav")
sound_game_over = pygame.mixer.Sound("./sounds/game_over.mp3")
sound_winner =pygame.mixer.Sound("./sounds/winner.mp3")

#Start of the program window
screen = pygame.display.set_mode(size)

##Lamba functions
background_update = lambda color: pygame.draw.rect(screen,background_level[color], [0,0,width,height]) # Lambda background update of the play area
draw_stick = lambda: pygame.draw.rect(screen,stick_color, [stick_position[0], stick_position[1], stick_position[2], stick_position[3]])  #Lambda bat update
draw_separate_score = lambda: pygame.draw.rect(screen,gray_borders, [(width), 0, 10, height_screen]) #Lambda separate area play line
draw_backgrund_score = lambda: pygame.draw.rect(screen,black, [(width + 10), 0, 166, height_screen]) #Lambda update background Score/lives
increase_live = lambda live: live + 1 #Lambda increase one live


def background_generator():
    """Function to generate a random background
    """
    random_background = random.randrange(0,len(background_level) - 1)
    screen.fill(background_level[random_background])
    return random_background

def random_sound_generator():
    """Function to generate random track for each level

    Returns:
        mp3: track random
    """
    random_num = random.randrange(0,4)
    random_sound = tracks_game[random_num]
    return random_sound

def random_position_ball():
    """Function to generate random ball position 
    """
    ball_position[0] = random.randrange(20 ,width - 20)
    random_direction = random.choice((-5,5))
    ball_direction[0] = random_direction
    ball_position[1] = 350

def checher_movement(lives):
    """Function that checks bat movement
Note: If the ball drops, I block the bat movement.
    """
    global ball_on_air, timer_event_adhere_ball, ball_sticky, extra_live

    key = pygame.key.get_pressed()
    if ball_position[1] + 8 <= stick_position[1]:
        if key[pygame.K_LEFT]:
            if stick_position[0] >= 0:
                stick_position[0] -= ball_position[2]
                if timer_status_adhere_ball and ball_on_air == False:
                    ball_position[0] -= ball_position[2]
            draw_stick()
        elif key[pygame.K_RIGHT]:
            if stick_position[0] + stick_position[2] < width:
                stick_position[0] += ball_position[2]
                if timer_status_adhere_ball and ball_on_air == False:
                    ball_position[0] += ball_position[2]
            draw_stick()            
        elif extra_live and lives < 3:
            extra_live = False
            return increase_live(lives)
    else:
        if ball_position[1] >= stick_position[1] + stick_position [3]:
            ball_direction[1] = 2
            ball_direction[0] = ball_direction[0] * 0.4
        if ball_position[1] >= height_screen:
            sound_fail.play()
            lives -= 1
            reset_parameters()
            time.sleep(1)
            return lives
    extra_live = False
    return lives

def reset_parameters():
    """Function to reset the parameters of the ball and bat
    """
    global timer_duration, timer_status, ball_on_air, ball_sticky, timer_status_stick_modified, timer_status_ball_modified, timer_event_adhere_ball,extra_live
    ball_position[0] = random.randrange(20 ,width - 20)
    random_direction = random.choice((-5,5))
    ball_direction[0] = random_direction
    ball_position[1] = 350
    ball_direction[1] = 5
    stick_position[0] = 500
    pill_position.clear()
    stick_position[2] = 120
    extra_live = False
    timer_status = False
    ball_on_air = True
    ball_sticky = False
    timer_status_stick_modified = False
    timer_status_ball_modified = False
    timer_event_adhere_ball = False

def decide_pills(color):
    """Function to select the event according to the color of each item

    Args:
        color (tuple): Receive tuple with random color
    """
    if color == red:
        if ball_direction[0] != -2 and ball_direction[0] != 2:
            modify_speed_ball(0.4)
    elif color == yellow:
        if stick_position[2] != 60:
            modify_stick(60)
            sound_stick[2].play()
    elif color == blue:
        global extra_live
        extra_live = True
    elif color == green:
        adhere_ball()
    elif color == white:
        if ball_direction[0] != -8 and ball_direction[0] != 8:
            modify_speed_ball(1.6)
    elif color == gray_borders:
        if stick_position[2] != 180:
            modify_stick(180)
            sound_stick[3].play()
    
def generate_random_pill(box_position):
    """Source to generate the probability of an item being drawn or not. Default < 15%

    Args:
    box_position (list): Receives the positions of the removed box.
    """
    random_probability = random.randrange(0,100)
    if len(pill_position) == 0 and random_probability > 85:
        global pill_random_color
        pill_random_color = pill_colors[random.randrange(0,len(pill_colors))]
        draw_pill(box_position)

def modify_stick(size):
    """Function to modify the bat size
    Args:
    value_score (int): Receives the length of the segment
    """
    global timer_status_stick_modified
    timer_status_stick_modified = True
    timer_duration = 10000
    pygame.time.set_timer(timer_event_stick,timer_duration)
    stick_position[2] = size
    timer_duration = 0

def check_timer(event):
    """function to control the state time before putting it back to normal"""
    global timer_status, timer_duration, ball_on_air, ball_sticky, timer_status_stick_modified, timer_status_ball_modified, timer_status_adhere_ball

    if timer_status_stick_modified:
        if event.type == timer_event_stick:
            stick_position[2] = 120
            timer_status_stick_modified = False
    if timer_status_ball_modified:
        if event.type == timer_event_ball and (ball_direction[0] == 2 or ball_direction [0] == -2) and (ball_direction[1] == 2 or ball_direction[1] == -2):
            ball_direction[0] = ball_direction[0] * 2.5
            ball_direction[1] = ball_direction[1] * 2.5
            timer_status_ball_modified = False
    if timer_status_ball_modified:
        if event.type == timer_event_ball and (ball_direction[0] == 7 or ball_direction [0] == -7) and (ball_direction[1] == 7 or ball_direction[1] == -7):
            ball_direction[0] = ball_direction[0] / 1.6
            ball_direction[1] = ball_direction[1] / 1.6
            timer_status_ball_modified = False
    if timer_status_adhere_ball:
        ball_sticky = True
        if event.type == timer_event_adhere_ball:
            if ball_on_air == False:
                ball_direction[1] = ball_direction[1] * - 1
            ball_on_air = True
            timer_status_adhere_ball = False
            ball_sticky = False

def draw_pill(box_position):
    """Function to draw the item's position
    Args:
    box_position (list)): Receives the position of the deleted box
    """
    pill_position.extend([box_position[0],box_position[1]])
    pygame.draw.circle(screen,pill_random_color,[pill_position[0] + pill_dimension ,pill_position[1] + pill_dimension],pill_dimension)
    pygame.draw.rect(screen,pill_random_color, [pill_position[0]+ pill_dimension, pill_position[1] , 40, 16])
    pygame.draw.circle(screen,pill_random_color,[pill_position[0] + 48,pill_position[1] + 8],pill_dimension)
    pill_position[1] += 2

def check_pill_colision():
    """Function to check whether the item collides with the bat or not
    """
    if (pill_position[1] + 8 ) >= stick_position[1] and stick_position[0] <= pill_position[0] + pill_dimension <= stick_position[0] + stick_position[2] + 5: 
        pill_position.clear()
        decide_pills(pill_random_color)
    elif(pill_position[1] + 45 >= height_screen):
        pill_position.clear()

def modify_speed_ball(multiply): #Value note: slower 0.4 = 2, faster:1.6 = 8
    """Function that modifies the speed of the ball
    Args:
        multiply (int): receives the multiplier that I apply to the speed
    """
    if (ball_direction[0] != 7 and ball_direction [0] != -7) and (ball_direction[1] != 2 and ball_direction[1] != -2):
        global timer_status_ball_modified
        timer_status_ball_modified = True
        timer_duration = 10000
        pygame.time.set_timer(timer_event_ball, timer_duration)
        ball_direction[0] = ball_direction[0] * multiply
        ball_direction[1] = ball_direction[1] * multiply
        timer_duration = 0

def adhere_ball():
    """Function to keep the ball stuck to the bat
    """
    global ball_sticky
    global timer_status_adhere_ball
    timer_status_adhere_ball = True
    ball_sticky = True
    timer_duration = 10000
    pygame.time.set_timer(timer_event_adhere_ball,timer_duration)
    timer_duration = 0
 
def draw_ball():
    """ Ball displacement function
    """
    if timer_status_adhere_ball and ball_on_air == False:
        pygame.draw.circle(screen,white,[ball_position[0],ball_position[1]],8)
    else:        
        pygame.draw.circle(screen,white,[ball_position[0],ball_position[1]],8)
        ball_position[0] += ball_direction[0]
        ball_position[1] += ball_direction[1]

def collisions_ball():
    """Function that detects collisions with walls and the bat. Checks whether it's sticky or not.
    """
    if (ball_position[1] +8 ) >= stick_position[1] and stick_position[0] -1 <= ball_position[0] <=(stick_position[0] + stick_position[2] + 1):
        if timer_status_adhere_ball and ball_sticky:
            global ball_on_air
            ball_on_air = False
            ball_position[1] = stick_position[1] - 8
        else:
            ball_direction[1] = ball_direction[1] * - 1
            sound_stick[0].play()        
    elif (ball_position[0] + 8) >= width or (ball_position[0] - 8)<= 0:
        ball_direction[0] = ball_direction[0] * - 1
        sound_walls[0].play()
    elif ball_position[1] <= 0:
        ball_direction[1] = ball_direction[1] * - 1
        sound_walls[0].play()
    
def update_score(value_score,i):
    """Function to add points
    Args:
    value_score (int): current points
    Returns:
    int: returns updated score
    """
    if 80 <= i <= 100:
        value_score += 200  
    elif 102 <= i <= 122:
        value_score += 180       
    elif 146 <= i <= 166:
        value_score += 150 
    elif 168 <= i <= 188:
        value_score += 120  
    else:
        value_score += 80       
    return value_score

def collisions_boxes(value_score,value_high_score):
    """Function that detects collisions with boxes
    Args:
    value_score (int): current score
    value_high_score (int): maximum score
    Returns:
    int: returns the updated scores
    """
    for box in box_list:
        if box[1]  <= ball_position[1] <= box[1] + box[3] and box[0] <= ball_position[0] <= box[0] + box[2]:
            generate_random_pill(box)
            box_list.remove(box)
            ball_direction[1] = ball_direction[1] * - 1
            sound_blocks.play()
            current_score = update_score(value_score,box[1])
            if current_score >= value_high_score:
                value_high_score = current_score
            return [current_score, value_high_score]
    return [value_score, value_high_score]