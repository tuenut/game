from app.utils.arguments import parse_arguments
from app.utils.logger import configure_logger
from app.utils.appmodes import main_mode, editor_mode

from config import *

if __name__ == "__main__":
    logger = configure_logger()
    start_opts = parse_arguments()

    logger.debug(f"Start with args <{start_opts}>.")
    logger.debug(f"Base dir: <{BASE_DIR}>.")

    if start_opts.editor_mode:
        editor_mode()
    else:
        main_mode()
