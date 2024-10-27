# class P:
#     def m(self):
#         print('this is m method of class P')
       
# class C(P):
#     def m1(self):
#         print('this is m1 metho of class C')    
# c= C()
# c.m()
# c.m1()

# class P:
#     a=10
#     #instance method
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print('this is instance method.')
#     @classmethod
#     def m2(self):
#         print('this is class method')
#     @staticmethod
#     def m3():
#         print('this is static method')
# class C(P):
#     pass

# c= C()
# print(c.a)
# c.m1()
# c.m2()
# c.m3()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print("Person eat momo")
    
# class employee(person):
#     def __init__(self, name, age,eno,esal):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#     def work(self):
#         print("Employee can work")
#     def empinfo(self):
#         print("employee name: ",self.name)
#         print("employee age: ",self.age)
#         print("employee employee number: ",self.eno)
#         print("employee salary: ",self.esal)
# e= employee('Ram',23,'e01',50000)
# e.eat()
# e.work()
# e.empinfo()


# class car:
#     def __init__(self,name,model,color):
#         self.name= name
#         self.model= model
#         self.color= color
#     def getinfo(self):
#         print(f'Car name : {self.name}\n Car model: {self.model}\n Car color: {self.color}')
        
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eatanddrink(self):
#         print("Person eat momo and drink coke")

# class employee(person):
#     def __init__(self, name, age,eno,esal,car):
#         super().__init__(name, age)
#         self.eno=eno
#         self.esal=esal
#         self.car=car
#     def work(self):
#         print('employee can work')
#     def empinfo(self):
#         print("employee name: ",self.name)
#         print("employee age: ",self.age)
#         print("employee employee number: ",self.eno)        
#         print("employee salary: ",self.esal)
#         print()
#         print('car details is:')
#         self.car.getinfo()

# c=car('Tesla','V2','Black')
# e= employee('Bhaskar',23,'e01',100000,c)
# e.empinfo()
# e.work()
# e.eatanddrink()

# #single inheritance
# class P:
#     def m1(self):
#         print('Parent class')
    
# class C(P):
#     def m2(self):
#         print('child class')
            
# c= C()
# c.m1()
# c.m2()

# # #multilevel inhericance
# class P:
#     def m1(self):
#         print('Parent class')
    
# class C(P):
#     def m2(self):
#         print('child class')

# class CC(C):
#     def m3(self):
#         print("Child child class")
        
# cc=CC()
# cc.m1()
# cc.m2()
# cc.m3()


# # #hiercical 
# class P:
#     def m1(self):
#         print('Parent class')
    
# class C1(P):
#     def m2(self):
#         print('First child class')

# class C2(P):
#     def m3(self):
#         print("Second child class")

# c=C1()
# c.m1()
# c.m2()

# cc=C2()
# cc.m1()
# cc.m3()
     
# # #Multiple 
# class P1:
#     def m1(self):
#         print('First Parent class')
    
# class P2():
#     def m2(self):
#         print('2nd Parent class')

# class C(P1,P2):
#     def m3(self):
#         print(" child class")

# c=C()
# c.m1()
# c.m2()
# c.m3()

#diamond problem
# class A:
#     def m1(self):
#         print('A class')
    
# class B(A):
#     def m1(self):
#         print('B class')

# class C(A):
#     def m1(self):
#         print("C class")
        
# class D(B,C):
#     def m1(self):
#         print("D class")

# d= D()
# d.m1()

# # MRO= Method Resolution Order Problem
# class A:
#     def m1(self):
#         print('A class')
    
# class B:
#     def m1(self):
#         print('B class')

# class C:
#     def m1(self):
#         print("C class")
        
# class X(A,B):
#     def m1(self):
#         print("X class")
        
# class Y(B,C):
#     def m1(self):
#         print("Y class")
        
# class P(X,Y,C):
#     def m2(self):
#         print("P class")

# p=P()
# p.m1()

# #super method
# class P:
#     def m1(self):
#         print("parent method")
# class C(P):
#     def m1(self):
#         super().m1()
#         print("child method")
# c= C()
# c.m1()

# class P:
#     a= 10
#     def __init__(self):
#         self.b=20
#         print("parent constructor is called")
#     def m1(self):
#         print("parent class instance method is called")
#     @classmethod
#     def m2(cls):
#         print("parent class class method is called")
#     @staticmethod
#     def m3():
#         print("parent class static method ")
    
# class C(P):
#     a=555
#     def __init__(self):
#         self.b=666 
#         print("child constructor is called")
#         super().__init__()  #call the parent class constructor
#         super().m1()
#         super().m2()
#         super().m3()
# c= C()
# print(c.b)
# print(c.a)

# class Person:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
#     def display(self):
#         print('Name:', self.name)
#         print('Age: ',self.age)

# class Student(Person):
#     def __init__(self, name, age,roll,marks):
#         super().__init__(name, age)
#         self.roll=roll
#         self.marks=marks
    
#     def display(self):
#         super().display()
#         print('ROll:', self.roll)
#         print('Marks: ',self.marks)
               
# s= Student('Bhaskar',20,101,99)
# s.display()

# class A:
#     def m1(self):
#         print('A class')
    
# class B(A):
#     def m1(self):
#         print('B class')

# class C(B):
#     def m1(self):
#         print("C class")
        
# class D(C):
#     def m1(self):
#         print("D class")
        
# class E(D):
#     def m1(self):
#         super().m1()
#         A.m1(self)
#         super(C,self).m1()  #Super method of C is called so m1 of B will be printed
#         print("E class")
# e= E()
# e.m1()


# class P:
#     a=10
#     def __init__(self):
#         self.b=20

# class C(P):
#     def m1(self):
#         print(super().a)
#         print(self.b)
# c= C()
# c.m1()

# class P:
#     def __init__(self):
#         print('parent class constructor')
#     # instance method
#     def m1(self):
#         print("parent class instance method")
#     @classmethod
#     def m2(cls):
#         print("parent class class method")
#     @staticmethod
#     def m3():
#         print("parent class static method")
        

# class C(P):
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
#     def m1(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# c= C()
# c.m1()


# class P:
#     def __init__(self):
#         print('parent class constructor')
#     # instance method
#     def m1(self):
#         print("parent class instance method")
#     @classmethod
#     def m2(cls):
#         print("parent class class method")
#     @staticmethod
#     def m3():
#         print("parent class static method")
        

# class C(P):
#     @classmethod
#     def m1(cls):
#         #we cannot access instance and constructor
#         # super().__init__()       #we cannnot access
#         # super().m1()             #we cannot access
#         super().m2()
#         super().m3()
#         super(C, cls).__init__(cls) #it calls constructor from parent class through child class
#         super(C,cls).m1(cls)
# c= C()
# c.m1()



class P:
    def __init__(self):
        print('parent class constructor')
    # instance method
    def m1(self):
        print("parent class instance method")
    @classmethod
    def m2(cls):
        print("parent class class method")
    @staticmethod
    def m3():
        print("parent class static method")
        

class C(P):
    @staticmethod
    def m1():
        super(C,C).m2()
        super(C,C).m3()
c= C()
c.m1()
