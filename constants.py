from ArcadeFont import ArcadeFont


class Constants:
    # Size of the window
    WINDOW_SIZE = (400, 800)
    X_CENTER = WINDOW_SIZE[0] / 2

    # Basic colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    UPDATE_INTERVAL = 5000

    DIR_L = -1
    DIR_R = 1

    # 2-point touch wall enumeration
    # Outside is for first side touch
    # Inside is for the second side touch
    ENEMY_NO_TOUCH = 0
    ENEMY_TOUCH_OUTSIDE = 1
    ENEMY_TOUCH_INSIDE = 2

    SPRITE_ENEMY_BULLET = {'spritesheet_filename': 'enemy_bullet.png',
                           'width': 8, 'height': 13, 'rows': 1, 'columns': 1}
    SPRITE_PLAYER_BULLET = {'spritesheet_filename': 'player_bullet.png',
                            'width': 8, 'height': 13, 'rows': 1, 'columns': 1}
    SPRITE_ENEMY_PLANE = {'spritesheet_filename': 'enemy.png',
                          'width': 31, 'height': 42, 'rows': 1, 'columns': 3}
    SPRITE_PLAYER_PLANE = {'spritesheet_filename': 'player.png',
                           'width': 64, 'height': 64, 'rows': 1, 'columns': 3}
    SPRITE_EXPLOSION = {'spritesheet_filename': 'explosion.png',
                        'width': 64, 'height': 64, 'rows': 3, 'columns': 8}
    SPRITE_DAMAGE = {'spritesheet_filename': 'player_damage.png',
                     'width': 20, 'height': 17, 'rows': 1, 'columns': 4}

    # Hordes formations
    FORMATIONS = {
        'v': [[1, 0, 0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 1, 0],
              [0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0]],
        'dv': [[1, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0]],
        'z': [[1, 1, 1, 1],
              [0, 0, 1, 0],
              [0, 1, 0, 0],
              [1, 1, 1, 1]],
        '/': [[0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, 1, 0, 0],
              [1, 0, 0, 0]],
        "\\": [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]
    }

    @staticmethod
    def get_available_text():
        inst = ArcadeFont(15).get_text("Press SPACE to fire. Press 'q' to quit",
                                       (0, 0, 124))
        game_over = ArcadeFont(35).get_text("GAME OVER", (0, 0, 124))
        restart = ArcadeFont(12).get_text(
            "Press 'r' to restart. Press 'q' to quit", (0, 0, 124))
        available_text = {
            "instructions": {
                'text': inst,
                'pos': inst.get_rect(center=(Constants.X_CENTER, 50))},
            "game_over": {
                'text': game_over,
                'pos': game_over.get_rect(center=(Constants.X_CENTER, 300))},
            "restart": {
                'text': restart,
                'pos': restart.get_rect(center=(Constants.X_CENTER, 340))

            }
        }
        return available_text


class Layer:
    PLAYER = 1
    PLAYER_BULLETS = 2
    ENEMIES = 3
    ENEMY_BULLETS = 4
    POWER_UPS = 5
    EXPLOSIONS = 9
