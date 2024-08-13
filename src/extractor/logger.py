import logging

"""
Other classes import log object from this class
"""
def __init_logger():
    # Create a logger object
    logger = logging.getLogger('LLMParserFramework')
    logger.setLevel(logging.DEBUG)
    
    # Create a console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # Define the logging format to include file name and line number
    formatter = logging.Formatter(
        '%(asctime)s: %(levelname)s: %(filename)s:%(lineno)d - %(message)s'
    )
    ch.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(ch)
    
    return logger

log = __init_logger()