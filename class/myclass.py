# class student:
#     '''This class is demo class. This class does nothing'''
#     #attributes/ variables
#     #behaviour/ methods()
#     def __init__(self, name, roll, marks):
#         self.name=name
#         self.roll= roll
#         self.marks= marks
        
#     def info(self):
#         print("hello my name is: ",self.name)
#         print("hello my roll no is: ",self.roll)
#         print("hello my marks is: ",self.marks)
# s= student('Bhaskar',23,90)
# s.info()
    
# list_of_std=[]

# while True:
#     name= input("enter name: ")
#     age= int(input("enter age: "))
#     marks= int(input("enter marks: "))
#     s= student(name, age, marks)
#     list_of_std.append(s)
#     print("info is added ")
#     option=input("do you want to continue to add? [yes/no]")
#     if option.lower()=='no':
#         break
    
# print('all stds info are: ')
# for s in list_of_std:
#     s.info()
#     print()

    
    


#print(A.__doc__) #it gives the doc string of the class which let us know what is abou the class is 


# class test:
#     a=10
#     def __init__(self):
#         self.b=20
    
#     def m1(self):
#         self.a=111
#         self.b=222
# t1=test()
# t2=test()
# t1.m1()
# test.a=111
# t1.b=222
# print(t1.a,t1.b)
# print(t2.a,t2.b)

# class test:
#     a=10
#     def __init__(self):
#         self.b=20
#     @classmethod
#     def m1(cls):
#         cls.a=111
#         cls.b=222
# t1=test()
# t2=test()
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(test.a,test.b)


#delete static variable

# class test:
#     a=10
#     @classmethod
#     def m1(cls):
#         del cls.a
# t1=test()
# t2=test()
# t1.m1()
# test.a=111
# t1.b=222
# print(t1.a,t1.b)
# print(t2.a,t2.b)

# class student:
#     def __init__(self, name , marks):
#         self.name= name
#         self.marks= marks
        
#     def display(self):
#         print('hi ',self.name)
#         print('your marks is ',self.marks)
        
#     def grade(self):
#         if self.marks>=60:
#             print('fist division')
#         elif self.marks>=50:
#             print('second division')
#         else:
#             print('failed')
            
# n= int(input('enter number of stds: '))
# for i in range(n):
#     name= input('enter your name: ')
#     marks= int(input('enter your marks: '))
#     s= student(name, marks)
#     s.display()
#     s.grade()
#     print()

#   #setter and getter

# class student:
#     def setName(self,name):
#         self.name= name
        
#     def getName(self):
#         return self.name
    
#     def setMarks(self,marks):
#         self.marks= marks
        
#     def getMarks(self):
#         return self.marks
# n= int(input('enter number of stds: '))
# for i in range(n):
#     s= student()
#     name= input('enter your name: ')
#     s.setName(name)
#     marks= int(input('enter your marks: '))
#     s.setMarks(marks)
#     print('hi ',s.getName())
#     print('your marks is ',s.getMarks())
#     print()

# class test:
#     count=0
#     def __init__(self):
#         test.count= test.count+1

# class ACEM:
#     department=4
#     @classmethod
#     def work(cls, name):
#         print(f'Acem has {cls.department} departments')
# ACEM.work('computer')       #classmethod so access through class name

# class outer:
#     def __init__(self):
#         print("outer class")
#     class inner:
#         def __init__(self):
#             print('inner classes')
#         def m(self):
#             print('inner class method')
# o= outer()
# i= o.inner()
# i.m()

class outer:
    def __init__(self):
        print("outer object is created")
    class inner:
        def __init__(self):
            print('inner object is created')
        class InnerInner:
            def __init__(self):
                print("innerinner object is created")
            def m(self):
                print('inner inner class')
                
o= outer()
i= o.inner()
ii= i.InnerInner()
ii.m()