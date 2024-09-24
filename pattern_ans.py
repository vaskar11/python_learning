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


# Q25   
for i in range(0,5):
    for j in range(i+1,0,-1):
        print(i+1,end="")
    print('')
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print('')
  