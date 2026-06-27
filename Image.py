import pygame
pygame.init()
SCREEN_WIDTH , SCREEN_HEIGHT = 500 , 500
display.surface = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Add background image and an image")
background_image = pygame.transform.scale(pygame.image.load('background.jpeg').convert(),((SCREEN_WIDTH , SCREEN_HEIGHT)))
penguin_image = pygame.transform.scale( pygame.image.load()
                                          