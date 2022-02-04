import sys

import pygame

from rocket_settings import Settings
from rocky import Rocky

import rocket_functions as r
def run_rocket():
    pygame.init()
    #initializing the game and creating a screen and settings
    r_settings = Settings()

    

    screen = pygame.display.set_mode((r_settings.screen_width,r_settings.screen_height))
    pygame.display.set_caption("Rocket Ship")

    #make a ship 
    rocky = Rocky(r_settings, screen)

    #setting the main loop for the game 
    while True:
        #watching out for mouse and keyboard movements 
        r.check_r_events(rocky)
        r.update_screen(r_settings, screen, rocky)
        #make the most recently drawn image visible
        rocky.update()
run_rocket()



