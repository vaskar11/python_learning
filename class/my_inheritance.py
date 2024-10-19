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


class car:
    def __init__(self,name,model,color):
        self.name= name
        self.model= model
        self.color= color
    def getinfo(self):
        print(f'Car name : {self.name}\n Car model: {self.model}\n Car color: {self.color}')
        
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatanddrink(self):
        print("Person eat momo and drink coke")

class employee(person):
    def __init__(self, name, age,eno,esal,car):
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print('employee can work')
    def empinfo(self):
        print("employee name: ",self.name)
        print("employee age: ",self.age)
        print("employee employee number: ",self.eno)        
        print("employee salary: ",self.esal)
        print()
        print('car details is:')
        self.car.getinfo()

c=car('Tesla','V2','Black')
e= employee('Bhaskar',23,'e01',100000,c)
e.empinfo()
e.work()
e.eatanddrink()
