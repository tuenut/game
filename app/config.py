import os
from logging import DEBUG, INFO

NAME = "game"


def init_base_dir_path():
    base_dir = os.path.dirname(__file__)

    while 'main.py' not in os.listdir(base_dir):
        base_dir = os.path.abspath(os.path.join(base_dir, '../'))

    return base_dir


BASE_DIR = init_base_dir_path()
LOG_DIR = os.path.join(BASE_DIR, '.logs')

REPO_TYPE = "json"
JSON_REPO = os.path.join(BASE_DIR, 'repo.json')
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
