import pygame

# Initialize mixer
pygame.mixer.init()

# Load music file
pygame.mixer.music.load('gameover.mp3')

# Play music
pygame.mixer.music.play()
