import pygame, sys
from pygame.locals import *
from constants import *
from ui import *


pygame.init()
d_surf = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('interface')

screen = Screen((0, 0), (1280, 720))
title = screen.add_textbox("abcdEFGH", (40, 40), (1200, 60), C1, C2)


def button1():
    print("test")


screen.add_button("test knop", (40, 340), (200, 50), C1, C3, C2, button1)


while True:
    m_pos = pygame.mouse.get_pos()
    d_surf.fill(BACKGROUND_COLOR)
    screen.draw(d_surf)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            for button in screen.buttons:
                if button.test(m_pos):
                    button.run()

    for button in screen.buttons:
        if button.test(m_pos):
            button.activated = True
        else:
            button.activated = False

    pygame.display.flip()
    pygame.time.Clock().tick(80)
