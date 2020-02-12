# todo: design config structure.
import os
import pygame

from logging import DEBUG, INFO

#############################
####  Base app settings  ####
#############################

NAME = "game"


def init_base_dir_path():
    base_dir = os.path.dirname(__file__)

    while 'main.py' not in os.listdir(base_dir):
        base_dir = os.path.abspath(os.path.join(base_dir, '../'))

    return base_dir


BASE_DIR = init_base_dir_path()
LOG_DIR = os.path.join(BASE_DIR, '.logs')

REPO_TYPE = "SQLITE"
SQLITE_REPO = os.path.join(BASE_DIR, 'sqlite_repo.db')

LOG_LEVEL = DEBUG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            '()': 'logging.Formatter',
            'format': '%(asctime)s [%(levelname)-8s] : %(message)s'
        },
        'verbose': {
            '()': 'logging.Formatter',
            'format': '%(asctime)s %(levelname)-8s [%(name)s:%(lineno)4d]: %(message)s'
        },
    },
    'loggers': {
        '': {
            'level': LOG_LEVEL,
            'handlers': ['basic_stream', 'basic_file'],
            'propagate': True,
        }
    },
    'handlers': {
        'basic_stream': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            "stream": "ext://sys.stdout"
        },
        'basic_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'maxBytes': 256 * 1024 * 1024,
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, '{}.log'.format(NAME))
        },
    }
}

#######################
####  Data config  ####
#######################

PLAYABLE_CHARACTER_TYPE = 0
NON_PLAYABLE_CHARACTER_TYPE = 1
CHARACTER_TYPES = (PLAYABLE_CHARACTER_TYPE, NON_PLAYABLE_CHARACTER_TYPE)
WEST = 0
EAST = 1
NORTH = 2
SOUTH = 3
DIRECTIONS = [WEST, EAST, NORTH, SOUTH]

####################
####  Controls  ####
####################

NAVIGATION = {
    pygame.K_LEFT: WEST,
    pygame.K_RIGHT: EAST,
    pygame.K_UP: NORTH,
    pygame.K_DOWN: SOUTH,
}

###########################
####  Render settings  ####
###########################

CELL_SIZE = 62 * 3
EXIT_HEIGHT = 8
EXIT_WIDTH = CELL_SIZE / 2
MAP_MARGIN_X = 5
MAP_MARGIN_Y = 5
CELL_BORDER = 1
COLOR_RENDER_BG = (0, 0, 0)
COLOR_LOCATION_BG = (100, 100, 100)
COLOR_EXIT_ACCESSIBLE = COLOR_LOCATION_BG
COLOR_EXIT_INACCESSIBLE = COLOR_RENDER_BG
FOG_OF_WAR = False

#######################
