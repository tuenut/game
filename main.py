from logging import getLogger
from logging.config import dictConfig
from app import App
from config import LOGGING


if __name__ == "__main__":
    logger = getLogger(__name__)
    dictConfig(LOGGING)

    try:
        App().run()
    except Exception as e:
        logger.exception("")
        exit(1)
