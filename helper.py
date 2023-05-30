import logging

"""
logger = logging.getLogger(__name__)
# logger.propagate = False will stop the logger from propagating to the parent logger/handlers.
logger.info('hello from helper')
"""

logger = logging.getLogger(__name__)

# Create Handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and Format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('(%name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning.')
logger.error('This is an error.')