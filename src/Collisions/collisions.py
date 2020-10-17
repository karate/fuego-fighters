import pygame
from src.Sprites import Explosion
from constants import Layer, Constants


def check_collisions(renderables, mixer):
    delete_out_of_bounds_bullets(renderables)

    player_layer_sprites = renderables.get_sprites_from_layer(Layer.PLAYER)
    if not player_layer_sprites:
        return

    # Sprite of the player's plane
    player_plane = player_layer_sprites[0]
    # A list with all the player's bullets
    player_bullets = renderables.get_sprites_from_layer(Layer.PLAYER_BULLETS)
    # A list with all the enemy planes
    enemy_planes = renderables.get_sprites_from_layer(Layer.ENEMIES)
    # A list with all the enemy bullets
    enemy_bullets = renderables.get_sprites_from_layer(Layer.ENEMY_BULLETS)
    # A list with all the power-ups
    power_ups = renderables.get_sprites_from_layer(Layer.POWER_UPS)

    # Check if the player has hit an enemy plane
    collision = pygame.sprite.spritecollideany(player_plane, enemy_planes,
                                               pygame.sprite.collide_mask)
    if collision:
        # Draw explosion
        explosion = get_explosion(Constants.SPRITE_EXPLOSION, collision.rect)
        renderables.add(explosion)
        mixer.play_sound('ship_explodes')
        # Reduce player HP to 0 so that the lifebar knows to finish animating and dying.
        player_plane.hit_points = 0
        # Remove player's plane
        player_plane.kill()
        # Remove enemy plane
        collision.kill()

    # Check if the player was hit by enemy fire
    collision = pygame.sprite.spritecollideany(player_plane, enemy_bullets,
                                               pygame.sprite.collide_mask)
    if collision:
        if player_plane.take_damage(10):
            # Draw explosion
            mixer.play_sound('ship_explodes')
            explosion = get_explosion(Constants.SPRITE_EXPLOSION,
                                      collision.rect)
            renderables.add(explosion)
        else:
            # Draw hit
            hit = get_explosion(Constants.SPRITE_DAMAGE, collision.rect)
            renderables.add(hit)

        # Remove enemy bullet
        collision.kill()

    # Check if enemy was hit by player's fire
    for enemy_plane in enemy_planes:
        collision = pygame.sprite.spritecollideany(enemy_plane, player_bullets,
                                                   pygame.sprite.collide_mask)
        if collision:
            # Remove enemy plane
            if enemy_plane.take_damage(10):
                # Draw explosion
                explosion = get_explosion(Constants.SPRITE_EXPLOSION,
                                          enemy_plane.rect)
                mixer.play_sound('ship_explodes')
                renderables.add(explosion)
            else:
                # Draw hit
                hit = get_explosion(Constants.SPRITE_DAMAGE, collision.rect)
                renderables.add(hit)

            # Remove player's bullet
            collision.kill()

    # Check if player has picked up power-up
    collision = pygame.sprite.spritecollideany(player_plane, power_ups,
                                               pygame.sprite.collide_mask)
    if collision:
        # TODO - implement power-up effect, depending on kind
    
        # Remove power-up from screen
        collision.kill()


# Returns an explosion object, at the specified position (rect)
def get_explosion(explosion_type, position):
    delay = 4 if explosion_type == Constants.SPRITE_EXPLOSION else 5
    explosion = Explosion(explosion_type, delay)
    explosion.rect = pygame.Rect(position)
    return explosion


def delete_out_of_bounds_bullets(renderables):
    # Player bullets
    player_bullets = renderables.get_sprites_from_layer(Layer.PLAYER_BULLETS)
    for bullet in player_bullets:
        if bullet.rect.y < 0:
            bullet.kill()

    # Enemy bullets
    enemy_bullets = renderables.get_sprites_from_layer(Layer.ENEMY_BULLETS)
    for bullet in enemy_bullets:
        if bullet.rect.y > pygame.display.get_surface().get_height():
            bullet.kill()

    enemies = renderables.get_sprites_from_layer(Layer.ENEMIES)
    for enemy in enemies:
        if enemy.rect.y > pygame.display.get_surface().get_height():
            enemy.kill()
