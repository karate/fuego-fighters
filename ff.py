
import pygame
from plane import Plane
from explosion import Explosion

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
  #This will be a list that will contain all the sprites we intend to use in our game.
  all_sprites_list = pygame.sprite.Group()

  # Load player's planeimages
  player_plane_image_top = pygame.image.load("resources/plane_top.png").convert_alpha()
  player_plane_image_left = pygame.image.load("resources/plane_left.png").convert_alpha()
  player_plane_image_right = pygame.image.load("resources/plane_right.png").convert_alpha()

  # Create player's plane
  player_plane = Plane(player_plane_image_top, player_plane_image_left, player_plane_image_right)
  player_plane.rect.x = (pygame.display.get_surface().get_width() - player_plane.rect.right) / 2
  player_plane.rect.y = pygame.display.get_surface().get_height() - 100
  # Add player's plane to sprite list
  all_sprites_list.add(player_plane)

  # Create explosion
  # Explosion(filename, rows, columns, width, height, delay)
  explosion = Explosion('resources/explosion.png', 3, 8, 64, 64, 2)
  explosion.rect.x = 100
  explosion.rect.y = 100
  # Add explosion to sprite list
  all_sprites_list.add(explosion)

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
        player_plane.key_up()

    all_sprites_list.update()
    # Clear Screen
    screen.fill(WHITE)

    # Now let's draw all the sprites in one go.
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()

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

    # Number of frames per secong
    # 30fps generate flickering. Going with 60
    clock.tick(60)

# Initialize the game engine
pygame.init()

main()

