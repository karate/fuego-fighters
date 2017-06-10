
import pygame
import random

from plane import Plane
from enemy import Enemy
from explosion import Explosion
from bullet import Bullet
from collisions import *

def main():

  # DEFINES
  LAYER_PLAYER = 1
  LAYER_PLAYER_BULLETS = 2
  LAYER_ENEMIES = 3
  LAYER_ENEMY_BULLETS = 4
  LAYER_EXPLOSIONS = 9

  # Set window size
  window_size = (400, 800)

  # Basic colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)

  # Select the font to use, size, bold, italics
  font = pygame.font.SysFont('Calibri', 40, False, False)
  wpm_font = pygame.font.SysFont('Calibri', 15, False, False)

  # Loop until the user clicks the close button.
  done = False

  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()

  # Create screen
  screen = pygame.display.set_mode(window_size)

  pygame.display.set_caption("Fuego Fighters")

  # SPRITES
  # This is a sprite group that keeps all our sprites. It also supports layers.
  renderables = pygame.sprite.LayeredUpdates()

  # Create player's plane
  # Plane(spritesheet_filename, width, height, speed_h, speed_v, cooldown, hot_points)
  player_plane = Plane('player.png', 64, 64, 1, 3, 5, 4, 400, 30)
  player_plane.rect.x = (pygame.display.get_surface().get_width() - player_plane.rect.right) / 2
  player_plane.rect.y = pygame.display.get_surface().get_height() - 100
  # Add player's plane to sprite list
  renderables.add(player_plane, layer = LAYER_PLAYER)

  # Create 5 enemies
  for i in range(5):
    # Enemy(spritesheet_filename, width, height, speed_h, speed_v, cooldown. hit_points)
    enemy_plane = Enemy('enemy.png', 31, 42, 1, 3, 1, .3, 0, 20)
    enemy_plane.rect.x = random.randint(50, pygame.display.get_surface().get_width() - 50)
    enemy_plane.rect.y = random.randint(50, pygame.display.get_surface().get_height() - 200)
    pygame.time.set_timer(pygame.USEREVENT + i, random.randint(1000, 3000))
    # Add enemy plane to sprite list
    renderables.add(enemy_plane, layer = LAYER_ENEMIES)

  # -------- Main Program Loop -----------
  while not done:
    check_collisions(renderables)

    # --- Main event loop
    for event in pygame.event.get():  # User did something
      # If user clicked close
      if event.type == pygame.QUIT:
        # Flag that we are done so we exit this loop
        done = True

      # Reset player plane's sprite
      if event.type == pygame.KEYUP:
        player_plane.reset_sprite()
        player_plane.reset_weapon_colldown()

      enemy_planes = renderables.get_sprites_from_layer(LAYER_ENEMIES)
      for idx, enemy_plane in enumerate(enemy_planes):
        if event.type == pygame.USEREVENT + idx:
          bullet = enemy_plane.fire()
          renderables.add(bullet, layer = LAYER_ENEMY_BULLETS)

    # Get user's key presses
    pressed = pygame.key.get_pressed()
    # 'q' quits the application
    if pressed[pygame.K_q]:
      done = True
    # Arrows move the player's plane
    else:
      # If the player is still in the game
      if renderables.get_sprites_from_layer(LAYER_PLAYER):
        # Move right
        if pressed[pygame.K_RIGHT]:
          player_plane.move_right()
        # More left
        if pressed[pygame.K_LEFT]:
          player_plane.move_left()
        # Move up
        if pressed[pygame.K_UP]:
          player_plane.move_up()
        # Move down
        if pressed[pygame.K_DOWN]:
          player_plane.move_down()
        # Fire
        if pressed[pygame.K_SPACE]:
          # Create bullet
          bullet = player_plane.fire()
          if type(bullet) is Bullet:
            renderables.add(bullet, layer = LAYER_PLAYER_BULLETS)

    # Update all sprites in the main sprite group
    renderables.update()

    # Clear Screen
    screen.fill(WHITE)

    # Draw all sprites
    renderables.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong
    # 30fps generate flickering. Going with 60
    clock.tick(60)

# Initialize the game engine
pygame.init()

main()

