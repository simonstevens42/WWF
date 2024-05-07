import logging
import inspect
from datetime import datetime

logging.basicConfig(filename='logfile.log', encoding='utf-8', level=logging.INFO)


def log_msg(msg, level) -> None:
    caller = inspect.stack()[1].filename
    logger = logging.getLogger(__name__)
    msg_strg = F"{datetime.now()} - {caller} - {msg}"
    if "INFO" in level:
        logger.info(msg_strg)
    elif "WARNING" in level:
        logger.warning(msg_strg)
    elif "ERROR" in level:
        logger.error(msg_strg)
    elif "CRITICAL" in level:
        logger.critical(msg_strg)
