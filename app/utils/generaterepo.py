import logging

logger = logging.getLogger(__name__)

from config import JSON_REPO, REPO_TYPE
from app.game.data.jsonrepo.datageneration import generate_json_repo


def generate_repo(opts, ):
    if opts.generate_repo is not None:
        repo_type = REPO_TYPE if opts.generate_repo == "current" else opts.generate_repo

        logger.info("Start generation data for {} repository type.".format(repo_type.upper()))
        if repo_type == "json":
            generate_json_repo(JSON_REPO)

        logger.info("Generation complete.")

        exit(0)
