import pygame
from .sprite import Sprite
from .bullet import Bullet
from constants import Constants


class Plane(Sprite):
    # Constructor. Pass in three images of the plane
    def __init__(self, plane_type, speed_h, speed_v, cooldown, hp,
                 respect_borders=False):
        # Call the parent class (Sprite) constructor
        Sprite.__init__(self, plane_type)

        # Spritesheet must contain 3 sprites, with the following order
        if len(self.images) == 3:
            self.image_left = self.images[0]
            self.image_top = self.images[1]
            self.image_right = self.images[2]
        else:
            self.image_left = self.images[0]
            self.image_top = self.images[0]
            self.image_right = self.images[0]

        self.speed_h = speed_h
        self.speed_v = speed_v
        self.last_fire = pygame.time.get_ticks()
        self.cooldown = cooldown
        self.hit_points = hp
        # This variable get True when the player releases the fire button,
        # so we can reduce the cooldown temporary
        self.keyup = False

        # Set initial sprite
        self.image = self.image_top

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of
        # rect.x and rect.y
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.respect_borders = respect_borders

    def fire(self):
        # Calculate the last time the gun fired
        now = pygame.time.get_ticks()
        current_cooldown = self.cooldown

        # If meanwhile the player has released the fire button,
        # reduce the cooldown to half.
        if self.keyup:
            current_cooldown /= 2

        # If the cooldown has expired, fire the canons!
        # (aka: create a Bullet object)
        if now - self.last_fire >= current_cooldown:
            self.last_fire = now
            self.keyup = False
            bullet = Bullet(Constants.SPRITE_PLAYER_BULLET, 6, -1)
            bullet.rect.x = self.rect.x + (self.rect.width / 2)
            bullet.rect.y = self.rect.y - 10
            return bullet

    # Remember that the player has released the fire button,
    # so we can reduce the cooldown
    def reset_weapon_cooldown(self):
        self.keyup = True

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.kill()
            return True
        return False

    # Reset sprite to image_top
    def reset_sprite(self):
        self.image = self.image_top
        self.mask = pygame.mask.from_surface(self.image)

    def disappear(self):
        self.kill()

    # Basic movement
    def move_left(self):
        # Change sprite
        self.image = self.image_left
        self.mask = pygame.mask.from_surface(self.image)
        # Move left
        self.rect.x -= self.speed_h
        # Don't let it go off the borders
        if self.rect.x > 0:
            return Constants.ENEMY_NO_TOUCH
        else:
            # if respect_borders is set, don't go outside border (x = 0)
            if self.respect_borders:
                self.rect.x = 0
                return Constants.ENEMY_TOUCH_OUTSIDE
            if self.rect.x > - self.rect.width:
                return Constants.ENEMY_TOUCH_OUTSIDE
            else:
                return Constants.ENEMY_TOUCH_INSIDE

    def move_right(self):
        # Change sprite
        self.image = self.image_right
        self.mask = pygame.mask.from_surface(self.image)
        # Move right
        self.rect.x += self.speed_h
        # Don't let it go off the borders
        screen_width = pygame.display.get_surface().get_width()
        sprite_width = self.image.get_width()
        if self.rect.x < screen_width - sprite_width:
            return Constants.ENEMY_NO_TOUCH
        else:
            if self.respect_borders:
                self.rect.x = screen_width - sprite_width
                return Constants.ENEMY_TOUCH_OUTSIDE
            if self.rect.x < screen_width:
                return Constants.ENEMY_TOUCH_OUTSIDE
            else:
                return Constants.ENEMY_TOUCH_INSIDE

    def move_up(self):
        # Move up
        self.rect.y -= self.speed_v
        # Don't let it go off the borders
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self):
        # Move down
        self.rect.y += self.speed_v
        # Don't let it go off the borders
        screen_height = pygame.display.get_surface().get_height()
        sprite_height = self.image.get_height()
        if self.rect.y > screen_height - sprite_height:
            self.rect.y = screen_height - sprite_height
            # Return false if the plane has reached the border
            return False
        return True
