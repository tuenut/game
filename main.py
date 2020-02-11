from app.utils.arguments import parse_arguments
from app.utils.logger import configure_logger
from app.utils.generaterepo import generate_repo
from app.utils.main import main

from config import *

if __name__ == "__main__":
    logger = configure_logger()
    start_opts = parse_arguments()

    logger.debug("Start with args %s" % start_opts)
    logger.debug(f"{BASE_DIR}")

    generate_repo(start_opts)

    main()

