from constants import Constants
from .bullet import Bullet
from .plane import Plane


class Enemy(Plane):
    def __init__(self, speed_h, speed_v, cooldown, hit_points, x=0, y=0):
        # Call the parent class (Plane) constructor
        Plane.__init__(self, Constants.SPRITE_ENEMY_PLANE, speed_h, speed_v,
                       cooldown, hit_points)
        self.rect.x = x
        self.rect.y = y
        # Choose the direction randomly 1 for right, -1 for left
        # self.direction = random.choice(
        #     [Constants.DIRECTION_L, Constants.DIRECTION_R]
        # )
        self.direction = Constants.DIR_L
        self.towards = {Constants.DIR_L: self.move_left,
                        Constants.DIR_R: self.move_right}

    def update(self):
        """Update plane movement

        :return:
        """
        # If hit bounds, change direction
        if self.towards[self.direction]() == Constants.ENEMY_TOUCH_INSIDE or \
                not self.move_down():
            self.disappear()

    def change_direction(self):
        """Change to opposite direction

        :return:
        """
        self.direction *= -1

    def fire(self):
        """Fire the bullet!

        :return:
        """
        bullet = Bullet(Constants.SPRITE_ENEMY_BULLET, 6, 1)
        bullet.rect.x = self.rect.x + (self.rect.width / 2)
        bullet.rect.y = self.rect.y - 10
        return bullet
