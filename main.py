import pygame
import gameScript.levels
import gameScript.system
import gameScript.draw
#Program start
pygame.init()
pygame.mixer.init()

#Window title
pygame.display.set_caption("ArKanoid")

#Game start
background = gameScript.system.background_generator()
gameScript.system.random_position_ball()
gameScript.system.start_game_sound.play(loops=-1)
gameScript.draw.start_game()

#Screen refresh rate control
clock = pygame.time.Clock()
#Main variables
run = True  #Main loop execution status
game_status = False #Game execution state

def definelevels():
    """Function that saves the randomly chosen background for each level
    Returns:
    (tuple) - Returns a tuple with the background color from a list
    """
    background = gameScript.system.background_generator()
    return background

def update_game(background):
    """Main function to constantly update the screen
    Args:
    background (tuple): Receive tuple color of the displayed background.
    """
    scores_updates = gameScript.system.collisions_boxes(gameScript.draw.score_nums.name,gameScript.draw.high_score_nums.name)
    gameScript.draw.score_nums.name = scores_updates[0]
    gameScript.draw.high_score_nums.name = scores_updates[1]    
    gameScript.system.background_update(background)
    gameScript.system.draw_separate_score()
    gameScript.system.draw_backgrund_score()
    gameScript.draw.update_sidebar()
    gameScript.levels.draw_boxes_level(gameScript.draw.level)
    gameScript.system.draw_ball()
    gameScript.system.collisions_ball()
    if len(gameScript.system.pill_position) != 0:    
        gameScript.system.draw_pill(gameScript.system.pill_position)
        gameScript.system.check_pill_colision()
    gameScript.system.draw_stick()
    pygame.display.flip()
    clock.tick(60)

def main_function_start_game():
    """Function join main process to start game when pressed Enter key
    """
    global game_status, background, current_track
    if game_status == False:
        game_status = True
        gameScript.draw.load_score()
        gameScript.system.start_game_sound.stop()
        current_track = gameScript.system.random_sound_generator()
        gameScript.draw.show_init_level(2)
        current_track.play(loops=-1)
        background = definelevels()   
        gameScript.levels.create_level(gameScript.draw.level)

def main_function_reset_highScore():
    """"Function to erase hihg-Score data
    """         
    if game_status == False:
        pygame.time.set_timer(gameScript.system.timer_event_reset_highScore,1500)
        gameScript.draw.save_high_score(0) 
        gameScript.draw.draw_reset_highScore_message()

def main_function_throw_sticky_ball():
    """Function to shoot the ball when it's sticked to the bat
    """
    if game_status and gameScript.system.timer_status_adhere_ball and gameScript.system.ball_on_air == False:
        gameScript.system.ball_direction[1] = gameScript.system.ball_direction[1] * - 1
        gameScript.system.ball_direction[0] = gameScript.system.ball_direction[0] * -1
        gameScript.system.ball_on_air = True
        gameScript.system.ball_sticky = False
        gameScript.system.sound_stick[0].play()

def main_function_control_game_boxes():
    """Function to check left boxes----Increase level, reset level or winner game
    """
    global game_status,background,current_lives, current_track
        #check if boxes = 0
    if len(gameScript.system.box_list) == 0:
        level = gameScript.draw.level
        level += 1
        current_track.stop()
        gameScript.system.sound_clear_level.play()
        gameScript.draw.clear_level(level)
        gameScript.system.reset_parameters()
        #check you passed game
        if level > gameScript.draw.final_level:
            gameScript.system.sound_winner.play()
            gameScript.draw.show_status_game('CONGRATULATIONS: you completed the game', 40)
            gameScript.system.sound_winner.stop()
            game_status = False
            set_box_colors = set(gameScript.system.box_colors)
            gameScript.system.box_colors = set_box_colors
            gameScript.system.box_list.clear()
            gameScript.system.reset_parameters()
            gameScript.system.start_game_sound.play(loops=-1)
            gameScript.draw.start_game()
        else:    
            gameScript.draw.show_init_level(gameScript.draw.lives)
            background = definelevels()
            gameScript.levels.create_level(level)
            current_track = gameScript.system.random_sound_generator()
            current_track.play(loops=-1)
    current_lives = gameScript.system.checher_movement(gameScript.draw.lives)

def main_function_control_lives():
    """Function to check left lives --- game over, reset level, increase live
    """
    global game_status, current_track,current_lives,background
    if current_lives < 0:
        current_track.stop()
        gameScript.system.sound_game_over.play()
        gameScript.draw.show_status_game('GAME OVER', 100)
        gameScript.system.sound_game_over.stop()
        game_status = False
        set_box_colors = set(gameScript.system.box_colors)
        gameScript.system.box_colors = set_box_colors
        gameScript.system.box_list.clear()
        gameScript.system.reset_parameters()
        gameScript.system.start_game_sound.play(loops=-1)
        gameScript.draw.start_game()     
    elif gameScript.draw.lives != current_lives and current_lives < gameScript.draw.lives:
        gameScript.draw.lives = current_lives
        current_track.stop()
        gameScript.draw.show_init_level(gameScript.draw.lives)
        gameScript.system.reset_parameters()
        current_track.play(loops=-1)
        update_game(background)
    elif gameScript.draw.lives != current_lives and current_lives > gameScript.draw.lives:
        gameScript.draw.lives = current_lives
        gameScript.draw.current_lives.name = current_lives
        update_game(background)
    #reset to the start game
    elif game_status == False:
        pass
    #update at every moment
    else:
        update_game(background)

########################
#MAIN GAME LOOP
########################
while run:
    for event in pygame.event.get():
        key = pygame.key.get_pressed() 

        # control quit game
        if event.type == pygame.QUIT:
            run = False

        #Game start
        gameScript.system.check_timer(event)
        if key[pygame.K_RETURN]:            
            main_function_start_game()
        elif key[pygame.K_r]:
            main_function_reset_highScore()
        elif event.type == gameScript.system.timer_event_reset_highScore and game_status == False:                    
                gameScript.draw.start_game()
        elif key[pygame.K_SPACE]:
            main_function_throw_sticky_ball()

    #Active game
    if game_status:
        main_function_control_game_boxes()
        #ckeck lives
        main_function_control_lives()
#Close the window
pygame.quit()