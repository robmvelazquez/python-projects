import logging


"""
Example 1 : All messages will display the time and date in the format as specified.

    # import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


Example 2 : 

    # Use this to display a message.
    logger = logging.getLogger(__name__)
    # logger.propagate = False will stop the logger from propagating to the parent logger/handlers.
    logger.info('hello from helper')


Example 3 : The stream handler logs all messages of level 'WARNING' and above. In this scenario, warning
                and error are output in the terminal. The file handler outputs the message of level 'ERROR'
                in the file named 'file.log'.

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

    Example 4 :

"""



""" 
===== LOGGERS ===== 
- named entities that provide an interface to interact with the logging framework.
 
===== HANDLERS ===== 
- defines where log messages should be sent.
- process log records received from loggers and directs to the corresponding outputs
    (console, files, emails, or external services).
 
===== FORMATTERS ===== 
- specify the layout and structure of log messages as well as timestamps, log levels, logger names,
    and custom message content.
 
===== LOG LEVELS ===== 
- represent severity or importance of log messages [debug, info, warning, error, critical] 
 
===== FILTERS =====
- provide further control for log record processing by handlers. able to include/exclude log records
    based on specific criteria such as logger names, log levels or custom attributes.

"""