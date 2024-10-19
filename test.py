# print(__file__)
# import os
# print(os.path.dirname(__file__))

# __name__
#This is added to every python file internally.

# <------------------------------->
# import math
# print(dir(math))
# help(math)
# print(math.sinh(30.6))
# import random 
# for i in range(10):
#     print(random.randint(1,6))
#     # print(random.randrange(10,20,2))
# print(random.uniform(1000,2000)) #gives float value in between range.

# from random import *
# list =['Bhaskar','Pragyan','Sumita','Nikita','Dipesh']
# print(choice(list))



# OTP generation of six numbers.
from random import *
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

# OR

otp=''
for i in range(6):
    otp=otp+ str(randint(0,9))
print(otp)



