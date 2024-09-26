# Q1
for i in range(1,6):
    for j in range(1,6):
        print("@",end=" ")
    print("")
    
# Q2    
for i in range(0,5):
    for j in range(i):
        print("",end=" ")
    for k in range(5-i):
        print('#', end="")
    print("")

# Q3
for i in range(5,0,-1):
    for j in range(i):
        print("@",end=" ")
    print("")
    
# Q4
for i in range(1,6):
    for j in range(i):
        print('#',end=" ")
    print("")

# Q5    
for i in range(1,6):
    print(" "*(5-i),end="")
    print("@"*i)

# Q6
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print('')

# Q7
for i in range(0,5):
    for j in range(5,0,-1):
        print(j, end="")
    print("")
  
# Q8
for i in range(5,0,-1):
    for j in range(0,5):
        print(i, end="")
    print("")

# Q9 
for i in range(1,6):
    for j in range(0,5):
        print(i, end="")
    print("")
   
# Q10  
for i in range(1,6):
    for j in range(i):
        print(j+1, end="")
    print("")
     
      
# Q11   
for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end="")
    print('')

# Q12
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end='')
    print("")

# Q13   
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print('')
    

# Q14   
for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j,end="")
    print('')
    

# Q15  
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print('')
   
# Q16   
for i in range(0,5):
    for j in range(i):
        print("",end=" ")
    for k in range(5-i):
        print(k+1, end="")
    print("") 
  
# Q.17 Pattern
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    #printing ascending part
    for j in range(1,i+1):
        print(j,end="")
    #printing decending part  
    for j in range(i-1,0,-1):
        print(j,end="")    
    print("")

# Q18
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    
    for j in range(1, i+1):
        print(j, end="")
    
    for k in range(i-1,0,-1):
        print(k,end="")   
    print()

# Q19
n=6
for i in range(1,n+1):
    print(" "*(n-i),end="")
    
    for j in range(1, i+1):
        print("*",end="")
    
    for k in range(i-1,0, -1):
        print("*", end="")      
    print()


# Q20
n=4
current_num = 1 #starting number
for i in range(1, n+1):
    for j in range(i):
        print(current_num,end="")
        current_num+=1
    print()
        
# Q21
n=4
for i in range(n):
    num=1
    for j in range(i+1):
        print(num, end="")
        # Calculate the next binomial coefficient (Pascal's Triangle)
        num = num * (i - j) // (j + 1)
    print()


# Q22
alph= ['A','B','C','D']
for i in range(4):
    for j in range(i+1):
        print(alph[i],end="")
    print()

# Q23
n=5
alph= ['A','B','C','D','E']
for i in range(1, n+1):
    print(" "*(n-i),end="")
    
    for j in range(i):
        print(alph[j],end="")
    
    for k in range(i-2,-1,-1):
        print(alph[k],end="")
    print()
        
# Q24
n=5
alph= ['A','B','C','D','E']
for i in range(n):
    print(" "*i,end="")
    
    for j in range(i,n):
        print(alph[j], end="")
        
    for k in range(n-2,i-1,-1):
        print(alph[k],end="")   
    print()

# Q25   
for i in range(0,5):
    for j in range(i+1,0,-1):
        print(i+1,end="")
    print('')
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print('')
 
 