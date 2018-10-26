from .sprite import Sprite


class Explosion(Sprite):
    # Constructor. Pass in three images of the plane
    def __init__(self, explosion_type, delay):
        # Call the parent class (Sprite) constructor
        Sprite.__init__(self, explosion_type)

        self.image_index = 0
        self.timer = 0
        self.animation_delay = delay

        self.image = self.images[0]

    def update(self):
        self.timer += 1
        if self.timer > self.animation_delay:
            self.timer = 0
            self.image_index += 1
            if self.image_index < len(self.images):
                self.image = self.images[self.image_index]
            else:
                self.kill()
