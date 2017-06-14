class Constants:
    # Size of the window
    WINDOW_SIZE = (400, 800)
    X_CENTER = WINDOW_SIZE[0] / 2

    # Basic colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    UPDATE_INTERVAL = 5000

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


class Layer:
    PLAYER = 1
    PLAYER_BULLETS = 2
    ENEMIES = 3
    ENEMY_BULLETS = 4
    EXPLOSIONS = 9