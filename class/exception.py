# print("hello")
# print(10/0)
# print('hello')

# print("this is my first line of program")
# try: 
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("this is my last line of program")

# try:
#     x= int(input("enter 1st number: "))
#     y= int(input("enter 2nd number: "))
#     print("Result of division is: ",x/y)
# except ZeroDivisionError as b:
#     print("type of exception: ",b)
# finally:
#     print('This is cleanup acitivites')
# import os
# try:
#     print('try')
#     os._exit(0)
# except:
#     print('except')
# finally:
#     print('finally')

# try:
#     print("outer try block")
#     try:
#         print("Inner try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("inner except block")
#     finally:
#         print("inner finally block")
#         print(10/0)
# except:
#     print("outer except block")
# finally:
#     print("outer finally block")

# try:
#     print("try block")
#     print(10/0)
# except:
#     print('except block')
# else:
#     print('else block')
# finally:
#     print("finally block")
         
class TooYoungExcption(Exception):
    def __init__(self, args):
        self.msg=args
        
class TooOldExcption(Exception):
    def __init__(self, args):
        self.msg=args
age= int(input("enter your age: "))
if age>60:
    raise TooOldExcption("Oh! Wait some more year to go to heaven")
elif age<18:
    raise TooYoungExcption("Still a kiddo child")
else:
    print("Work alot man, you need to earn more.")