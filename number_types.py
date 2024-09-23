import math
# #loop through numbers from 1 to 100
# print("Prime numbers from 1 to 100")
# for num in range(2,100): #as 1 is not a prime number starting with 2
    
#     isprime= True
#     for i in range(2, num):
#         if num%i==0:
#             isprime = False
#             break
#     if isprime:
#         print(num, end=" ")
# print(" ")
# print("<--------output end for this program---------->")


# #check a number is prime or not:
# a= int(input("enter a number:"))
# for i in range(2,a):
#     is_prime= True
#     if a% i==0:
#         is_prime= False
#         break  
# if is_prime:
#     print("prime number")
# else:
#     print("not a prime number")
    
# print("<--------output end for this program---------->")


# #to check storng number: 145= 1! + 4! + 5!
# def is_strong(number):
#     #convert the number to string to get each digit
#     digits= str(number)
#     sum=0
#     for j in range(0,len(digits)):
#         sum= sum +math.factorial(int(digits[j]))
#     return sum

# num= int(input("enter a number: "))
# if is_strong(num)== num:
#     print("strong number")
# else:
#     print("not a strong number")
  
    
# #to check palindrome number
# def is_palindrome(number):
#     digits= str(number)
#     return digits[::-1]

# nums= int(input("enter a number: "))
# if is_palindrome(nums):
#     print("palindrome number")
# else:
#     print("not a palindrome number")


# # perfect number divisor are added to get the number as 6 is perfect number divisor of 6(1+2+3)=6
# def is_perfect(number):
#     sum= 0
#     for i in range(1, number):
#         if number%i == 0:
#             sum+= i
#     return sum

# nums= int(input("enter a number: "))
# if is_perfect(nums)== nums:
#     print("perfect number")
# else:
#     print("not a perfect number")
    
    
# #armstrong number: 153: 1^3 + 5^3 + 3^3
# def is_armstrong(number):
#     sum=0
#     digits= str(number)
#     l= len(digits)
#     for i in range(0, l):
#         sum= sum + int(digits[i])** l
#     return sum
# nums1= int(input("enter a number: "))
# if is_armstrong(nums1)== nums1:
#     print("armstrong number")
# else:
#     print("not a armstrong number")


# #fibonacci series
# a,b= 0,1
# fibo=[]
# n= int(input('enter number of terms: '))
# print("the fibonacci series are:")
# print(a, end=" ")
# for num2 in range(0,n):
#     print(b,end=" ")
#     a,b=b,a+b


# #nth number fibonacci series:
# a,b= 0,1
# fibo=[]
# n= int(input('enter nth number: '))
# print(f"the {n}th fibonacci series is:")
# for num2 in range(0,n):
#     a,b=b,a+b
# print(a)


#harshad number as:21 is also a Harshad number because 2+1=3 and 21/3=7
def is_harshad(number):
    digits= str(number)
    sum= 0
    for i in range(0, len(digits)):
        sum+= int(digits[i])
    if number% sum==0:
        return True
    else: return False
    
nums4= int(input("enter a number: "))
if is_harshad(nums4):
    print("harshad number")
else:
    print("not a harshad number")
    
    

