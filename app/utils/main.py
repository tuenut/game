import logging

logger = logging.getLogger(__name__)

from app import App


def main():
    try:
        App().run()
    except Exception as exception:
        logger.exception("Some exception on `App().run()`.")

        raise exception
