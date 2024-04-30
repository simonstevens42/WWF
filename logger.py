import logging
from datetime import datetime


def log_msg(msg, level):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='logfile.log', encoding='utf-8', level=logging.INFO)
    if "INFO" in level:
        logger.info(F"{datetime.now()} - {msg}")
    elif "WARNING" in level:
        logger.warning(F"{datetime.now()} - {msg}")