from app.mainfunctions.arguments import parse_arguments
from app.mainfunctions.logger import configure_logger
from app.mainfunctions.generaterepo import generate_repo
from app.mainfunctions.main import main

if __name__ == "__main__":
    logger = configure_logger()
    start_opts = parse_arguments()

    logger.debug("Start with args %s" % start_opts)

    generate_repo(start_opts)

    main()

