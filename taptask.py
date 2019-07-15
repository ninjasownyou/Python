"""Approximate dimensions of usable space are 1024 x ~526"""

import pygame
from pygame.locals import *
from pygame import freetype

# Define color variables
#rgbdef = [(255, 0, 0), (249, 115, 6), (255, 255, 20), (21, 176, 26), (3, 67, 223), (126, 30, 156)]
rgbdef = [(125,57,3)]
header_color = rgbdef[0]
body_color = rgbdef[0]

# Define class objects

# Initialize
pygame.init()
#pygame.display.set_icon()
pygame.freetype.init()
screen = pygame.display.set_mode()
screen.fill(rgbdef[0])
pygame.display.set_caption('Don\'t forget!')
pygame.display.flip()

# Define variables
done = False
font = pygame.freetype.SysFont('segoeuisymbol', size=16)

# Blit everything to the screen
"""screen.blit(header, (0, 0))
screen.blit(body, (0, 60))
pygame.display.flip()"""

# Set up variables we'll use throughout main loop
frame_count = 0
frame_rate = 30
clock = pygame.time.Clock()
tstamp = 0
w_center = screen.get_width() // 2
h_center = screen.get_height() // 2
print(w_center)
print(h_center)

# Loops gameplay until quit inputs set done = True
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # Timer Count-up
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    time_string = "{0:02}:{1:02}".format(minutes, seconds)
    timer_rect = font.render_to(screen, (w_center, h_center), time_string, fgcolor=(0, 0, 0), bgcolor=header_color, size=26)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
quit()
