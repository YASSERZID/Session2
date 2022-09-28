from project1.module1 import add
# insteas of 

import logging

logger = logging.getLogger(__name__)

def say_hello():
    logger.info('hello world!')

add(2, 2)