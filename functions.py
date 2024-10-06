
# def sum_sub(a,b):
#     sum=a+b
#     sub= a-b
#     return sum,sub
# t= sum_sub(20,10)
# print(t)
# a,b=sum_sub(20,10)
# print(f"sum is {a} and sub is {b}")

# def sum(*n):
#     total=0
#     for x in n:
#         total+=x
#     print("sum is: ", total)
    
# sum()
# sum(10,20)
# sum(10,20,30,40)

# def f( *agrs,**kwargs):
#     print(agrs)
#     print(kwargs)
        
# f(10,20,30,a=10,b=20,c=30)


# a=10    #global variable
# def f1():
#     a=222
#     b=20    #local variable
#     print(a)
#     print(globals().get('a'))
#     print(globals()['a'])  
# f1()

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter number"))
# a=fact(n)
# print(f'Factorial of {n} is :',a)

# s=lambda n:n*n  # when we assign s then it is not a anonymous function
# print("The square is: ",s(4))

# s=lambda a,b,c: a if a>b and a>c else b if b>c else c
# # print("biggest number is: ",s(20,30,40))

# #Here We fliter even number from a range
# l= range(1,10)
# def isEven(n):
#     if n%2==0:
#         return True
#     else: return False
# l1=[]
# for n in l:
#     if isEven(n) == True:
#         l1.append(n)
# print(l1)

# #now by using fliter function
# def iseven(n):
#     if n%2==0:
#         return True
#     else: return False
    
# l= range(1,10)
# l1=list(filter(iseven, l))
# print(l1)

# #now use of lambda function
# l= range(1,10)
# l1= list(filter(lambda x:x%2==0, l))
# print(l1)

# l = range(1, 6)
# def double(x):
#     return 2 * x
# l1 = list(map(double, l))
# print(l1)

# l= range(1,6)
# l1= list(map(lambda x:x*x,l))
# print(l1)

# from functools import reduce
# l=range(1,6)
# sum=reduce(lambda x,y:x+y,l)
# print(sum)

# def hello(name):
#     print("Hello",name)
# wish= hello #another name as wish to the fucntion.
# hello('bhaskar')
# wish('isha')

def outer():
    print("outer function.")
    def inner():
        print("inner function")
    inner()
    print('outer function calling inner function')
    

