import pygame
from explosion import Explosion

# DEFINES
LAYER_PLAYER = 1
LAYER_PLAYER_BULLETS = 2
LAYER_ENEMIES = 3
LAYER_ENEMY_BULLETS = 4
LAYER_EXPLOSIONS = 9

def check_collisions(renderables):
  delete_out_of_bounds_bullets(renderables)

  player_layer_sprites = renderables.get_sprites_from_layer(LAYER_PLAYER)
  if not player_layer_sprites:
    return

  # Sprite of the player's plane
  player_plane = player_layer_sprites[0]
  # A list with all the player's bullets
  player_bullets = renderables.get_sprites_from_layer(LAYER_PLAYER_BULLETS)
  # A list with all the enemy planes
  enemy_planes = renderables.get_sprites_from_layer(LAYER_ENEMIES)
  # A list with all the enemy bullets
  enemy_bullets = renderables.get_sprites_from_layer(LAYER_ENEMY_BULLETS)

  # Check if the player has hit an enemy plane
  collision = pygame.sprite.spritecollideany(player_plane, enemy_planes, pygame.sprite.collide_mask)
  if collision:
    # Draw explosion
    explosion = get_explosion(collision.rect)
    renderables.add(explosion)
    # Remove player's plane
    player_plane.kill()
    # Remove enemy plane
    collision.kill()

  # Check if the player was hit by enemy fire
  collision = pygame.sprite.spritecollideany(player_plane, enemy_bullets, pygame.sprite.collide_mask)
  if collision:
    if player_plane.take_damage(10):
      # Draw explosion
      explosion = get_explosion(collision.rect)
      renderables.add(explosion)
    else:
      # Draw hit
      hit = get_hit(collision.rect)
      renderables.add(hit)

    # Remove enemy bullet
    collision.kill()

  # Check if enemy was hit by player's fire
  for idx, enemy_plane in enumerate(enemy_planes):
    collision = pygame.sprite.spritecollideany(enemy_plane, player_bullets, pygame.sprite.collide_mask)
    if collision:
      # Remove enemy plane
      if enemy_plane.take_damage(10):
        # Draw explosion
        explosion = get_explosion(collision.rect)
        renderables.add(explosion)
      else:
        # Draw hit
        hit = get_hit(collision.rect)
        renderables.add(hit)

      # Remove player's bullet
      collision.kill()

# Returns an explosion object, at the specified position (rect)
def get_explosion(position):
  explosion = Explosion('explosion.png', 64, 64, 3, 8, 4)
  explosion.rect = pygame.Rect(position)
  return explosion

def get_hit(position):
  explosion = Explosion('player_damage.png', 20, 17, 1, 4, 5)
  explosion.rect = pygame.Rect(position)
  return explosion

def delete_out_of_bounds_bullets(renderables):
  # Player bullets
  player_bullets = renderables.get_sprites_from_layer(LAYER_PLAYER_BULLETS)
  for bullet in player_bullets:
    if bullet.rect.y < 0:
      bullet.kill()

  # Enemy bullets
  enemy_bullets = renderables.get_sprites_from_layer(LAYER_ENEMY_BULLETS)
  for bullet in enemy_bullets:
    if bullet.rect.y > pygame.display.get_surface().get_height():
      bullet.kill()
