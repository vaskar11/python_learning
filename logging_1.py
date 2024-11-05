# print(10/0)
# assert (10>2)
# print('All okay')


# def squareit(x):
#     return x**x

# assert squareit(3)==9,"code is ok till now"

# print(squareit(2))  #4
# print(squareit(3))  #9
# print(squareit(4))  #16

import logging
# #logging.basicConfig(format='%{levelname}s:%{name}s:%{message}s',filename="log.txt",level=10,filemode='w',datefmt='%d/%m/%Y')

# logging.basicConfig(
#     format='%(levelname)s:%(name)s:%(message)s',
#     filename="log.txt",
#     level=logging.DEBUG,
#     filemode='w',
#     datefmt='%d/%m/%Y'
# )

# print('This is demo of logging')
# logging.debug('This code is corrected')
# logging.warning('this is only information')
# logging.error("this is error information")
# logging.critical("this is critical information")


# logging.basicConfig(filename='abc.txt', level= logging.WARNING)
# logging.info("Process started")
# try:
#     x= int(input('Enter 1st number: '))
#     y= int(input('Enter 2nd number: '))
#     print('The result is: ',x/y)
# except ZeroDivisionError as z:
#     print('Probably there is zero division error.You need to check your log file for more info. ')
#     logging.exception(z)
# except ValueError as v:
#     print('Probably there is value error.You need to check your log file for more info. ')
#     logging.exception(v)
# logging.info("Process completed")

# logger=logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
# filehandler= logging.FileHandler('vaskar.log',mode='w')
# formatter= logging.Formatter('%(asctime)s: %(levelname)s:%(name)s: %(message)s:')
# filehandler.setFormatter(formatter)
# logger.addHandler(filehandler)
# logger.critical('This is critical message')
# logger.error('This is error message')
# logger.warning('This is warning message')
# logger.info('This is info message')
# logger.debug('This is debug message')

# import logging
# # logging.basicConfig(filename='log.txt',level=logging.DEBUG, filemode='w')
# logging.basicConfig(format='%(asctime)s:%(levelname)s: %(name)s: %(message)s',filename='log.txt',filemode='w',level= logging.DEBUG,datefmt='%A %B %d/%m/%Y %H:%M:%S')
# print('This is demo of logging')
# logging.debug('This code is corrected')
# logging.info('This code only information')
# logging.warning('this is warning information')
# logging.error("this is error information")
# logging.critical("this is critical information")


''' we need 3 object to be made: formatter, handler, and logger'''

import logging
logger= logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
filehandler= logging.FileHandler('bhaskar.log',mode='w')
formatter= logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.critical("This is critical message")
logger.error("This is error message")
logger.warning("This is warning message")
logger.debug("This is debug message")
logger.info("This is info message")

