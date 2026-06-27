import logging
from logging.handlers import RotatingFileHandler
from .constants import LOG_DIR


# verifica existencia da pasta de logs
LOG_DIR.mkdir(parents=True, exist_ok=True)

formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(message)s'
)


def setup_logger(name, file_name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        LOG_DIR / file_name,
        maxBytes=5_000_000,
        backupCount=5,
        encoding='utf-8'
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def addlog(name, message):
    """Usado para adicionar logs"""

    new_log = setup_logger(name, f'{name}.log')
    new_log.info(message)
