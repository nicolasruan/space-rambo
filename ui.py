import pygame
from constants import *

class Screen:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.buttons = []
        self.displays = []
        self.items = []
        
    def add_button(self, text, pos, size, color1, color2, color3, action):
        pos0, pos1 = pos
        size0, size1 = size
        refx, refy = self.pos
        pos = [pos0 + refx, pos1 + refy]
        b = Button(text, pos, size, color1, color2, color3, action)
        self.buttons.append(b)
        return b

    def add_textbox(self, text, pos, size, color1, color2):
        pos0, pos1 = pos
        refx, refy = self.pos
        pos = [pos0 + refx, pos1 + refy]
        d = TextBox(text, pos, size, color1, color2)
        self.items.append(d)
        return d

    def draw(self, d_surf):
        for b in self.buttons:
            b.draw(d_surf)
        for d in self.items:
            d.draw(d_surf)

    def set_visible(self, visible):
        for b in self.buttons:
            b.visible = visible
        for d in self.items:
            d.visible = visible

    def clear(self):
        self.buttons = list()
        self.items = list()


class TextBox:
    def __init__(self, text, pos, size, color1, color2):
        self.text = text
        self.pos = pos
        self.size = size
        self.center = [int(pos[0] + size[0]/2), int(pos[1] + size[1]/2)]
        self.color = color1
        self.text_color = color2
        self.visible = True

    def draw(self, d_surf):
        if self.visible:
            pos0, pos1 = self.pos
            size0, size1 = self.size
            r = Rect(pos0, pos1, size0, size1)
            pygame.draw.rect(d_surf, self.color, r)
            t = FONT.render(self.text, True, self.text_color)
            t_rect = t.get_rect()
            t_rect.center = self.center
            d_surf.blit(t, t_rect)

    def clear(self):
        self.text = list()

    def set_text(self, text):
        self.text = text


class Button:
    def __init__(self, text, pos, size, color1, color2, color3, action):
        self.text = text
        self.pos = pos
        self.size = size
        self.center = [int(pos[0] + size[0]/2), int(pos[1] + size[1]/2)]
        self.color = color1
        self.color2 = color2
        self.text_color = color3
        self.action = action
        self.activated = False
        self.visible = True

    def run(self):
        self.action()

    def draw(self, d_surf):
        if self.visible:
            pos0, pos1 = self.pos
            size0, size1 = self.size
            t = None
            if self.activated:
                pygame.draw.rect(d_surf, self.color2, (pos0, pos1, size0, size1))
                t = FONT.render(self.text, True, self.text_color)
            else:
                pygame.draw.rect(d_surf, self.color, (pos0, pos1, size0, size1))
                t = FONT.render(self.text, True, self.text_color)

            t_rect = t.get_rect()
            t_rect.center = self.center
            d_surf.blit(t, t_rect)
        
    def test(self, pt):
        size = self.size
        pt2 = self.pos
        return Rect(pt2[0], pt2[1], size[0], size[1]).collidepoint(pt)
