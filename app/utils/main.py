import logging

logger = logging.getLogger(__name__)

from app import App


def main():
    try:
        App().run()
    except Exception as e:
        logger.exception("")
        exit(1)
