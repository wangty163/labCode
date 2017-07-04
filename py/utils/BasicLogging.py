import logging
# %(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s
logging.basicConfig(format='%(asctime)s [%(levelname)s]:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)