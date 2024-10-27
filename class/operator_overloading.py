# print(10+20)
# print("Hello"+" World")

# class book:
#     def __init__(self,pages):
#         self.pages= pages
#     def __add__(self,other):
#         return self.pages+ other.pages
#     def _gt__(self,other):
#         return self.pages>other.pages
    
# # - = __sub__(self,other)
# # *= __mul__(self,other)
# # /= __div__(self,other)
# # //= __floordiv__(self,other)
# # %= __mod__(self,other)
# # **= __pow__(self,other)
# # += = __iadd__(self,other)
# # -= = __isub__(self,other)
# # > = __gt__(self,other)
# # < = __lt__(self,other)

         
# b1= book(200)
# b2= book(100)
# print(b1+b2)
# print(b1>b2)

# class employee:
#     def __init__(self,name, salary):
#         self.name=name
#         self.salary= salary
#     def __mul__(self,other):
#         return self.salary* other.days

# class attendencesheet:
#     def __init__(self,name,days):
#         self.name= name
#         self.days= days
        
# e= employee('Bhaskar',5000)
# t= attendencesheet("Bhaskar",15)
# print("total salary:",e*t)      #here e has the magic method so it should come at 1st

# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll= roll
#         self.marks= marks
#     def __str__(self):
#         return f"This is {self.name} object"

# s1= Student('Bhaskar',101,90)
# s2= Student('Dipesh',202,89)
# print(s1)
# print(s2)

# class book:
#     def __init__(self,pages):
#         self.pages= pages
#     def __add__(self,other):
#         # return self.pages+ other.pages
#         return book(self.pages+ other.pages)
#     def __str__(self):
#         return f"Total number of pages: {self.pages}"

#     def __mul__(self,other):
#         print("this is multiplication")
#         return self.pages*other.pages

# b1= book(200)
# b2= book(100)
# b3= book(400)
# b4=book(500)
# print(b1+b2+b3)
# print(b1+b2*b3+b4)

# # not possible as python overwrite to the last m1 function
# class test:
#     def m1(self):
#         print("no-arg method")
#     def m1(self,a):
#         print("1 arg method")
#     def m1(self,a,b):
#         print("2 arg method")
# a= test()
# a.m1()
# a.m1(10)
# a.m1(10,20)

# class Test:
#     def sum(self,*args):
#         total=0
#         for x in args:
#             total+=x
#         print("Sum is: ",total)
        
# t=Test()
# t.sum(10,20)


# # method overriding
# class p:
#     def property(self):
#         print('Gold + Land + Cash')
#     def wife(self):
#         print("Katrina")
# class c(p):
#     def wife(self):
#         print("Kajol")        

# c= c()
# c.property()
# c.wife()

# # constructor overriding
# class p:
#     def __init__(self):
#         print("parent constructor")
# class c(p):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")

# c=c()


class duck:
    def talk(self):
        print('Quack Qucak')
class dog:
    def talk(self):
        print("Bhaw Bhaw")
class cat:
    def talk(self):
        print("Meow Meow")
class goat:
    def talk(self):
        print("Myaa Myaa")

def f1(obj):
    obj.talk()

l= [duck(),dog(),cat(),goat()]
for obj in l:
    f1(obj)