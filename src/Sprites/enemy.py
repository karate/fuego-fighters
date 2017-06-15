from .plane import Plane
from .bullet import Bullet


class Enemy(Plane):
    def __init__(self, width, height, rows, columns, speed_h, speed_v,
                 cooldown, hit_points, x=0, y=0, spritesheet_filename='enemy.png'):
        # Call the parent class (Plane) constructor
        Plane.__init__(self, spritesheet_filename, width, height,
                       rows, columns, speed_h, speed_v, cooldown, hit_points)
        self.rect.x = x
        self.rect.y = y
        # Choose the direction randomly 1 for right, -1 for left
        self.direction = -1  # [-1, 1][random.randint(0, 1)]
        self.TOWARDS = {-1: self.move_left, 1: self.move_right}

    def update(self):
        # If hit bounds, change direction
        if not self.TOWARDS[self.direction]():
            self.change_direction()
        if not self.move_down():
            self.disappear()

    def change_direction(self):
        self.direction *= -1

    def fire(self):
        bullet = Bullet('enemy_bullet.png', 8, 13, 1, 1, 6, 1)
        bullet.rect.x = self.rect.x + (self.rect.width / 2)
        bullet.rect.y = self.rect.y - 10
        return bullet
