import logging.config
from logger_config import LOGGING
import mylib

def main()->None:    
    logging.config.dictConfig(LOGGING)
    logging.getLogger(__name__).warning('Started')
    mylib.do_something()
    logging.getLogger(__name__).warning("End")


if __name__=='__main__':
    main()