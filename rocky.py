import pygame

class Rocky():
    def __init__(self,r_settings, screen):
        self.screen = screen
        self.r_settings = r_settings
        #When working with a rect object, you can use the x- and y-coordinates
        #of the top, bottom, left, and right edges of the rectangle, as well as the center
     
        #load the rocket image and get its rect
        self.image = pygame.image.load("D:/Project learning AI/Rocket/images/rocket_1.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #make the rocket sit in the middle of the screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        #self.center = float(self.rect.centery)
        #movingtag
        self.moving_right = False
        self.moving_left = False 
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """update rocket's position on flag's movement """
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.center += self.r_settings.rocket_speed_factor
        if self.moving_left and self.rect.left> 0:
            self.center -= self.r_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.r_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.r_settings.rocket_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center                  


    def blitme(self):
        """ Draw the ship in its current position """
        self.screen.blit(self.image, self.rect)
