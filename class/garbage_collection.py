import gc

# class test:
#     def __init__(self):
#         print("this is constructor")
#     def __del__(self):
#         print("this is destrutor")
        
# l=[test(),test(),test()]

# class engine:
#     a= 10
#     def __init__(self):
#         self.b= 20
#     def m1(self):
#         print("This is engine. ")
    
# class car:
#     def __init__(self):
#         self.engine= engine()
#     def m2(self):
#         print('Car object using engine object')
#         print(self.engine.a)
#         self.engine.m1()
#         print(self.engine.b)

# c= car()
# c.m2()

# class car:
#     def __init__(self,name,model,color):
#         self.name= name
#         self.model= model
#         self.color= color
#     def getinfo(self):
#         print(f'Car name : {self.name}\n Car model: {self.model}\n Car color: {self.color}')
        
# class employee:
#     def __init__(self,ename, eno, car):
#         self.ename= ename
#         self.eno=eno
#         self.car= car
#     def empinfo(self):
#         print("Employee name: ",self.ename)
#         print("Employee number: ",self.eno)
#         print("Employee car information: ")
#         self.car.getinfo()
        
# c= car('Tesla','V2','Red')
# e= employee('Bhaskar',23,c)
# e.empinfo()
