import sys
import pygame 

def check_r_events(rocky):
    """responding to mouse and keyboard events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, rocky)
                
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, rocky)




def check_keydown_events(event, rocky):
    if event.key == pygame.K_RIGHT:
        rocky.moving_right = True

    elif event.key == pygame.K_LEFT:
        rocky.moving_left = True

    elif event.key == pygame.K_UP:
        rocky.moving_up = True

    elif event.key == pygame.K_DOWN:
        rocky.moving_down = True

def check_keyup_events(event, rocky):
    if event.key == pygame.K_RIGHT:
        rocky.moving_right = False   
    elif event.key == pygame.K_LEFT:
        rocky.moving_left = False
    elif event.key == pygame.K_UP:
        rocky.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocky.moving_down = False                     
def update_screen(r_settings, screen, rocky):
    """Update images on the screen and flip to the new screen."""
    screen.fill(r_settings.bg_color)
    rocky.blitme()
    #making the most recently drawn thing visible
    pygame.display.flip()