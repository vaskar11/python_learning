from abc import abstractmethod,ABC
# class Test:
#     @abstractmethod
#     def m1():
#         pass
    
# class vehicle(ABC):
#     @abstractmethod
#     def noofwheels(self):
#         pass
    
# class bus(vehicle):
#     def noofwheels(self):
#         return 6
# b= bus()
# print(b.noofwheels())

# class test:
#     def m1(self):
#         print("This is not abstract method")
#     @abstractmethod
#     def m2(self):
#         print("Hello")
    
# class subtest(test):
#     def m2(self):
#         print("This is m2 method")
        
# t= subtest()
# t.m1()
# t.m2()

# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#     @abstractmethod
#     def m3(self):
#         pass
# class dipeshimplementation(A):
#     def m1(self):
#         print('m1')
#     def m2(self):
#         print('m2')
#     def m3(self):
#         print('m3')

# class biplovimplementation(A):
#     def m1(self):
#         print('m1')
#     def m2(self):
#         print('m2')
#     def m3(self):
#         print('m3')
# class nikitaimplementation(A):
#     def m1(self):
#         print('m1')
#     def m2(self):
#         print('m2')
#     def m3(self):
#         print('m3')

# d= dipeshimplementation()
# d.m1()
# d.m2()
# d.m3()


# x=10      #public
# _x= 10    #protected
# __x=10    #private

# class test:
#     def __init__(self):
#         self.__x=10
#     def __m1(self):
#         print("This is public method")
#     def m2(self):
#         print(self.__x)
#         self.__m1()
# t= test()
# t.m2()
# print(t._test__x)       #name mandling as only name is changed with underscore.
# # t.m1()


class account:
    def __init__(self, min_balance):
        self.__balance= min_balance
    def getbalance(self):
        #validation code
        return self.__balance
        
        
a= account(200)
print(a.balance)