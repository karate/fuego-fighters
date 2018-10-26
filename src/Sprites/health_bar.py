from pygame import Rect
from pygame import Surface
from pygame.draw import rect as draw_rect
from pygame.sprite import Sprite

from constants import Constants


class HealthBar(Sprite):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.max = self.parent.hit_points
        self.hit_points = self.parent.hit_points

    def update(self, *args):
        if self.parent.hit_points < self.hit_points:
            self.hit_points -= 0.5
        if self.hit_points <= 0:
            self.kill()

    @property
    def image(self):
        width = self.parent.rect.width
        height = Constants.HP_BAR_HEIGHT
        img = Surface((width, height))
        img.fill(Constants.INERT)
        damage = int(self.hit_points / self.max * width)
        draw_rect(img, Constants.DAMAGE, Rect(0, 0, damage, height))
        health = int(self.parent.hit_points / self.max * width)
        draw_rect(img, Constants.HP, Rect(0, 0, health, height))
        return img

    @property
    def rect(self):
        r = Rect(0, 0, self.parent.width, Constants.HP_BAR_HEIGHT)
        r.midtop = self.parent.rect.midbottom
        return r
