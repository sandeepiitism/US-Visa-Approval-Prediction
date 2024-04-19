import os
import sys

from us_visa.logger import logging
from us_visa.exception import USvisaException

## logger test
# logging.info("This is test for logging working")

## exception test
try:
    a = 1/"10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e