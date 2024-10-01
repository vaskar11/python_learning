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
 
 # Q26
alph= 'NEPAL'
for i in range(0,len(alph)+1):
    for j in range(i):
        print(alph[j], end="")
    print()
for i in range(5,0,-1):
    for j in range(j):
        print(alph[j],end="")
    print()
    
# Q27
alph= ['A','B','C','D']
for i in range(0,4):
    for j in range(i+1):
        print(alph[i],end="")
    print()
for i in range(2,-1,-1):
    for j in range(i+1):
        print(alph[i],end="")
    print()


# Q28
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
    
# Q29
for i in range(1,6):
    print(" "*i, end="")
    for j in range(i,n):
        print(j,end="")
    for k in range(n,i-1,-1):
        print(k,end="")
    print()
    
# Q30
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
 
# Q31
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()

# Q32
n=6
for i in range(1,n+1):
    for sp in range(n,i,-1):
        print(' ',end="")
    for j in range(1,i+1):
        print(i,end=' ')    
    print()
    
# Q33
n=6
for i in range(1,n+1):
    for sp in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# Q34
n=7
for i in range(1,n+1):
    if i%2!=0:
        for sp in range(n,i,-1):
            print(' ',end='')
        for j in range(1, i+1):
            print('*',end=" ")
        print()

for i in range(2,n+1):
    if i%2!=0:
        for sp in range(i-1):
            print(' ',end='')
        for j in range(1, n-i+2):
            print('*',end=" ")
        print()  

# Q35
n=4
for i in range(1, n+1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    for k in range(2,i+1):
        print(k,end="")
    print()
    
for i in range(n-1,0,-1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    for k in range(2,i+1):
        print(k,end='')
    print()
  
# Q36
n=4
for i in range(1,n+1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='') 
    print()
    
for i in range(n-1,0,-1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    print()

# Q37
alph= ['A','B','C','D']
n=3
for i in range(0,n+1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(0,i+1):
        print(alph[j],end='')
    for k in range(i-1,-1,-1):
        print(alph[k],end='') 
    print()
    
for i in range(n-1,-1,-1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(0,i+1):
        print(alph[j],end='')
    for k in range(i-1,-1,-1):
        print(alph[k],end='')
    print()

# Q38
alph= ['A','B','C','D']
n=3
for i in range(0,n+1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(0,i+1):
        print(alph[j],end='')
    for k in range(i-1,-1,-1):
        print(alph[k],end='') 
    print()

# Q39
n=3  
alph= ['A','B','C','D']
for i in range(n,-1,-1):
    for sp in range(n-i):
        print(' ',end='')
    for j in range(0,i+1):
        print(alph[j],end='')
    for k in range(i-1,-1,-1):
        print(alph[k],end='')
    print()

# Q40
n=4
alph= ['A','B','C','D','E']
for i in range(0,n+1):
    print(" "*(n-i),end="")
    for j in range(0,i+1):
        print(alph[j],end='')
    print()
for i in range(n-1,-1,-1):
    print(" "*(n-i),end='')
    for j in range(0,i+1):
        print(alph[j],end='')
    print()

# Q41
n=4
alph= ['A','B','C','D','E']
for i in range(0,n+1):
    for j in range(i,-1,-1):
        print(alph[j],end='')
    print()
for i in range(n-1,-1,-1):
    for j in range(i,-1,-1):
        print(alph[j],end='')
    print()
   
# Q42
n=4
alph= ['A','B','C','D','E']
for i in range(n,-1,-1):
    for j in range(i,-1,-1):
        print(alph[j],end='')
    print()

Q43
n=6
start=9
for i in range(0,n+1):
    for j in range(0,i):
        print(start,end='')
        start+=1
        if(start==10):
            start=0
        
    print()

44
n=4
for i in range(0,n):
    for j in range(0,n-i):
        print(j+1,end='')
    for j in range(0,i):
        print("_",end='')
    for j in range(0,i):
        print("_",end='')
    for j in range(n-i,0,-1):
        print(j,end='')
      
        
    print()

45
n=5
for i in range(0,n):
    for j in range(0,int((2*n-2*(i+1))/2)):
        print(" ",end="")
    for j in range(0,2*i+1):
        print(j+1,end='')
    print()

# Q46
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()
    
# Q47
alph= ['A','B','C','D','E','F']
for i in range(6,-1,-1):
    for j in range(0,i):
        print(alph[j],end='')
    for k in range(i-1,-1,-1):
        print(alph[k],end='')
    print()
 
Q48  
n=5
for i in range(0,n):
    for j in range(0,int((2*n-2*(i+1))/2)):
        print(" ",end="")
    for j in range(0,2*i+1):
        print(i+1,end='')
    print()

#49
n=4
start=9
is9=False
for i in range(0,n):
    num=start
    for j in range(0,2*i+1):
        print(num,end='')
        if(num==9):
            is9=True
    
     
        if(is9):
            num-=1
        else:
            num+=1
    start-=1
    is9=False
        
    print()
 

Q50
n=5
temp=n
for i in range(0,n):
    
    for j in range(0,i+1):
        print(temp,end='')
        temp+=1
    temp=n-(i+1)
    print()
#Q51
n=5
start=n
isN=False
for i in range(0,n):
    num=start
    for j in range(0,2*i+1):
        print(num,end='')
        if(num==n):
            isN=True
       
     
        if(isN):
            num-=1
        else:
            num+=1
    start-=1
    isN=False
        
    print()
 
# Q58
n=5
for i in range(1,n+1):
    for j in range(5,i-1,-1):
        print(j,end='')
    print()

