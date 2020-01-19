import os
from logging import DEBUG

NAME = "game"

BASE_DIR = os.path.dirname(__file__)
LOG_DIR = os.path.join(BASE_DIR, '.logs')

REPO_TYPE = "json"
JSON_REPO = os.path.abspath("repo.json")

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
            'format': '%(asctime)s %(levelname)-8s [%(name)s.%(module)s:%(lineno)4d]: %(message)s'
        },
    },
    'loggers': {
        '': {
            'level': LOG_LEVEL,
            'handlers': ['basic_stream'],
            'propagate': True,
        }
    },
    'handlers': {
        'basic_stream': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
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
