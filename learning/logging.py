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

Example 4 : Utilize these lines of code with the logging.conf file.

    import logging.config   

    logging.config.fileConfig('logging.conf')

    logger = logging.getLogger('simpleExample')
    logger.debug('This is a debug message')

Example 5 : This can be utilized to monitor errors.

    try:
        a = [1,2,3]
        val = a[4]
    except: IndexError as e:
        logging.error(e, exc_info=True)

Example 6 : Rotating File Handler will output the INFO into a log file until reaching 2MB. When 2 MB is reached,
            a new log file will be generated, with a maximum of 5 log files at a time.

    import logging
    from logging.handlers import RotatingFileHandler

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
    logger.addHandler(handler)

    for _ in range(10000):
        logger.info('Hello, World!')

Example 7: Timed Rotating File Handler will output a rotating log file handler based on how much time has passed.
    
    import logging
    from logging.handlers import TimedRotatingFileHandler

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler('timed_test_log', when='s', interval=5, backupCount=5)
    logger.addHandler(handler)

    for _ in range(6):
        logger.info('Hello, World!')
        time.sleep(5)

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