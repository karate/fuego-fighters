from .sprite import Sprite


class Bullet(Sprite):
    # Constructor. Pass in three images of the plane
    def __init__(self, bullet_type, speed, direction):
        # Call the parent class (Sprite) constructor
        self._sprite = Sprite.__init__(self, bullet_type)

        self.width = bullet_type['width']
        self.height = bullet_type['height']
        self.speed = speed
        self.direction = direction

        self.image = self.images[0]

    def update(self):
        self.rect.y += self.speed * self.direction
