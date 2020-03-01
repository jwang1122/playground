import logging
log_format = '%(asctime)s %(levelname)s [%(name)s] - %(message)s::%(filename)s::%(lineno)d'
logging.basicConfig(filename='mylogs.log', filemode='w', level=logging.DEBUG, format=log_format)
logger = logging.getLogger('WANG')

from circle import circle_area

try:
    area = circle_area(-2)
    print("18:",area)
except ValueError as err:
    logger.info('Error: wrong input value')
