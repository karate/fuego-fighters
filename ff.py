
import pygame
import random

from plane import Plane
from enemy import Enemy
from explosion import Explosion
from bullet import Bullet

def main():

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
  enemy_renderables = pygame.sprite.LayeredUpdates()

  # Create player's plane
  # Plane(spritesheet_filename, width, height, speed_h, speed_v, cooldown)
  player_plane = Plane('player.png', 64, 64, 1, 3, 5, 4, 400)
  player_plane.rect.x = (pygame.display.get_surface().get_width() - player_plane.rect.right) / 2
  player_plane.rect.y = pygame.display.get_surface().get_height() - 100
  # Add player's plane to sprite list
  renderables.add(player_plane)

  # Create 5 enemies
  for i in range(5):
    # Enemy(spritesheet_filename, width, height, speed_h, speed_v)
    enemy_plane = Enemy('enemy.png', 31, 42, 1, 3, 1, .3)
    enemy_plane.rect.x = random.randint(50, pygame.display.get_surface().get_width() - 50)
    enemy_plane.rect.y = random.randint(50, pygame.display.get_surface().get_height() - 200)
    pygame.time.set_timer(pygame.USEREVENT + i, random.randint(1000, 3000))
    # Add enemy plane to sprite list
    enemy_renderables.add(enemy_plane)

  # Create explosion
  # Explosion(spritesheet_filename, rows, columns, width, height, delay)
  explosion = Explosion('explosion.png', 64, 64, 3, 8, 4)
  explosion.rect.x = 100
  explosion.rect.y = 100
  # Add explosion to sprite list
  renderables.add(explosion)

  # -------- Main Program Loop -----------
  while not done:
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

      for i in range(5):
        if event.type == pygame.USEREVENT + i:
          enemy_renderables.get_sprite(i).fire(renderables)

    # Get user's key presses
    pressed = pygame.key.get_pressed()
    # 'q' quits the application
    if pressed[pygame.K_q]:
      done = True
    # Arrows move the player's plane
    else:
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
          renderables.add(bullet)
        #print(bullet)

    # Update all sprites in the main sprite group
    renderables.update()
    enemy_renderables.update()

    # Clear Screen
    screen.fill(WHITE)

    # Draw all sprites
    renderables.draw(screen)
    enemy_renderables.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong
    # 30fps generate flickering. Going with 60
    clock.tick(60)

# Initialize the game engine
pygame.init()

main()

