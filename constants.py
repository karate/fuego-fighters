from ArcadeFont import ArcadeFont


class Constants:
    # Size of the window
    WINDOW_SIZE = (400, 800)
    X_CENTER = WINDOW_SIZE[0] / 2

    # Basic colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # UI Settings
    HP = GREEN
    DAMAGE = RED
    INERT = BLACK
    HP_BAR_HEIGHT = 3

    UPDATE_INTERVAL = 4500

    DIR_L = -1
    DIR_R = 1

    # SFX
    MUSIC_BACKGROUND = 'resources/background.wav'
    MUSIC_BACKGROUND_INTRO = 'resources/background_intro.wav'

    SOUNDS = {
        'player_bullet': 'resources/player_bullet.wav',
        'enemy_bullet': 'resources/enemy_bullet.wav',
        'ship_explodes': [
            'resources/explosion_0.wav',
            'resources/explosion_1.wav',
            'resources/explosion_2.wav',
        ]
    }

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
        title = ArcadeFont(20).get_text("Welcome to Fuego Fighters",
                                       (255, 0, 0))
        start = ArcadeFont(15).get_text("When ready, press SPACE to start.",
                                       (0, 0, 124))
        inst = ArcadeFont(15).get_text("Press SPACE to fire. Press 'q' to quit",
                                       (0, 0, 124))
        game_over = ArcadeFont(35).get_text("GAME OVER", (0, 0, 124))
        
        restart = ArcadeFont(12).get_text(
            "Press 'r' to restart. Press 'q' to quit", (0, 0, 124))
        quit = ArcadeFont(15).get_text("Press 'q' to quit", (0, 0, 124))
        available_text = {
            "start_menu": {
                "title":{
                    'text': title,
                    'pos': title.get_rect(center=(Constants.X_CENTER, 50))},
                "start": {
                    'text': start,
                    'pos': start.get_rect(center=(Constants.X_CENTER, 550))},
                "quit": {
                    'text': quit,
                    'pos': quit.get_rect(center=(Constants.X_CENTER, 720))}
                },
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
    UI = 8
    EXPLOSIONS = 9
