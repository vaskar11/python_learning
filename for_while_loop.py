s=['morning ','is','boring']
x=0
for i in s:
    print(f" the {x}th index element is {i}")
    x+=1
print("<----First output------>")

for x in range(10):
    if(x%2!=0): # find the odd number in range of 10
        print(x)
print("<----second output------>")

for i in range(3):
    for j in range(2):
        print(i,j)
print("<----third output------>")

n= int(input("enter number of rows "))
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print('')
print("<----Forth output------>")

#use of break 
for i in range(10):
    if i==5:
        break
    print(i)
print("break end")
print("<----First output------>")

#use of else with the loop
l=[10,20,30,600,400,2,4,300]
for i in l :
    if i>=500:
        print("you cannot buy this as it cross price 500")
        continue 
    print(i)    
else:
    print("this is else part of for loop")
print("shopping compeleted")
print("<----second output------>")

#while loop 
x=1
while x<=5:
    print(x)
    x+=1
print("<----third output------>")

#while loop with  divisible by 3 condition   
while x<=20:
    if (x%3==0):
        print(x)
    x+=1  
print("<----Forth output------>")

#finding of sum of number using while loop
x=1
sum=0
n= int( input("enter a number:"))
while x<= n:
    sum+=x
    x+=1
print(f"the sum of first {n} natural number is {sum}")   

#nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1


#infinite loop    
i=0
while True:
    print("hello ", i)
    i+=1
#this will print the hello infinte time as while True case is always true


name = input("enter a name: ")
while name!="bhaskar":
    name= input("enter another  name ")
print("thank u")


# pass operation
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    else:
        print(i)
        

#del operation
s="hello"
a=s #value of s assigned to a
b=a # value of a assigned to b
#now all 3 variable have same values "hello"
print(s)
del s 
# deleting s the value hello is not deleted only the refrence variable s which was pointing to hello is deleted.
print(a)
#so still a and b will print hello
print(b)