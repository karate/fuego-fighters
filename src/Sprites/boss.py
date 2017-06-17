from .bullet import Bullet
from .enemy import Enemy


class Boss(Enemy):
    def __init__(self, spritesheet_filename, width, height, rows, columns,
                 speed_h, speed_v, cooldown, hit_points):
        # Call the parent class (Plane) constructor
        Enemy.__init__(self, spritesheet_filename, width, height, rows,
                       columns, speed_h, speed_v, cooldown, hit_points)

        self.direction = -1

    def fire(self):
        # Bullet(spritesheet_filename, width, height, rows,
        # columns, speed, direction)
        bullet = Bullet('enemy_laser.png', 13, 59, 1, 1, 4, 1)
        bullet.rect.x = self.rect.x + (self.rect.width / 2)
        bullet.rect.y = self.rect.y + 100
        return bullet
