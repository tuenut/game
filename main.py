import os
from logging import getLogger
from logging.config import dictConfig
from app import App
from config import LOGGING, LOG_DIR


def configure_logger():
    logger = getLogger(__name__)

    try:
        os.mkdir(LOG_DIR)
    except OSError as e:
        if e.errno == 17:
            pass
        else:
            logger.exception('%s %s', e.strerror, e.filename)

    dictConfig(LOGGING)

    return logger


if __name__ == "__main__":
    logger = configure_logger()

    try:
        App().run()
    except Exception as e:
        logger.exception("")
        exit(1)
