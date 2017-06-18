"""
Main game file
"""
import pygame
from constants import Constants
from constants import Layer
from src.Collisions import check_collisions
from src.Sprites import Bullet
from src.Sprites import Plane
from src.exceptions import LevelFinished, FormationEnd
from src.map import Map


def main():
    """Creates the main window and calls the main loop function

    :return:
    """
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create screen
    screen = pygame.display.set_mode(Constants.WINDOW_SIZE)

    pygame.display.set_caption("Fuego Fighters")

    # SPRITES
    # This is a sprite group that keeps all our sprites.
    # It also supports layers.
    renderables = pygame.sprite.LayeredUpdates()

    player_plane = create_player_plane(renderables)
    # update_map(renderables)

    while main_loop(clock, player_plane, renderables, screen):
        # Reset renderables in order to be able to loop again
        renderables = pygame.sprite.LayeredUpdates()
        player_plane = create_player_plane(renderables)
        pygame.time.delay(500)


def create_player_plane(renderables):
    """ It creates the player plane

    :return: player_plane
    """
    # Create player's plane
    # Plane(spritesheet_filename, width, height, speed_h, speed_v,
    #       cooldown, hot_points)
    player_plane = Plane('player.png', 64, 64, 1, 3, 5, 4, 100, 30,
                         respect_borders=True)
    player_plane.rect.x = (pygame.display.get_surface().get_width() -
                           player_plane.rect.right) / 2
    player_plane.rect.y = pygame.display.get_surface().get_height() - 100
    # Add player's plane to sprite list
    renderables.add(player_plane, layer=Layer.PLAYER)
    return player_plane


def draw_text(screen, render):
    """Draw text on screen.

    :param screen: game screen
    :param render: comma separated string
    :return:
    """
    if render:
        for word in render.split(','):
            screen.blit(
                Constants.get_available_text()[word]['text'],
                Constants.get_available_text()[word]['pos']
            )


def main_loop(clock, player_plane, renderables, screen):
    """All game logic goes here

    :param clock:
    :param player_plane:
    :param renderables:
    :param screen:
    :param text:
    :return: True if user wants to restart, False otherwise
    """
    # Loop until the user clicks the close button.
    done = False
    restart = False

    last_update = 0
    _map = Map(renderables)
    text_to_render = "instructions"

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
                player_plane.reset_weapon_cooldown()

            enemy_planes = renderables.get_sprites_from_layer(Layer.ENEMIES)
            for idx, enemy_plane in enumerate(enemy_planes):
                if event.type == pygame.USEREVENT + idx:
                    bullet = enemy_plane.fire()
                    renderables.add(bullet, layer=Layer.ENEMY_BULLETS)

        # Get user's key presses
        pressed = pygame.key.get_pressed()
        # 'q' quits the application
        if pressed[pygame.K_q]:
            done = True
        if pressed[pygame.K_r]:
            restart = True
            done = True
        # Arrows move the player's plane
        else:
            # If the player is still in the game
            if renderables.get_sprites_from_layer(Layer.PLAYER):
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
                    if isinstance(bullet, Bullet):
                        renderables.add(bullet, layer=Layer.PLAYER_BULLETS)
            else:
                text_to_render = "game_over,restart"

        # Update all sprites in the main sprite group
        renderables.update()

        # Clear Screen
        screen.fill(Constants.WHITE)

        # Draw all sprites
        renderables.draw(screen)
        draw_text(screen, render=text_to_render)

        # Refresh Screen
        pygame.display.flip()

        now = pygame.time.get_ticks()
        if now - last_update >= Constants.UPDATE_INTERVAL and not _map.active:
            last_update = now
            text_to_render = None
            try:
                _map.start()
                horde = _map.next_horde()
                horde.activate()
            except LevelFinished:
                _map.pause()
        if _map.active and now - last_update >= horde.interval:
            last_update = now
            try:
                horde.render_line()
            except FormationEnd:
                _map.pause()

        # Number of frames per second
        # 30fps generate flickering. Going with 60
        clock.tick(60)
    if restart:
        return True
    return False


# Initialize the game engine
pygame.init()

main()
