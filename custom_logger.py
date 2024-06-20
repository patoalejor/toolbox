import logging
from colorlog import ColoredFormatter

def create_logger():    
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create console handler and set level to DEBUG, INFO
    ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # Create a colored formatter
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s %(levelname)-8s%(reset)s %(message)s",
        datefmt='%Y-%m-%d %H:%M',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    # Add the formatter to the handler
    ch.setFormatter(formatter)
    # Add the handler to the logger
    logger.addHandler(ch)

    logger = logging.getLogger(__name__)
    return logger


logger = create_logger()
logger.debug('This is the debug')
logger.info('This is the information')
logger.warning('This is the warning')
logger.error('This is the error')
logger.critical('This is the critical')