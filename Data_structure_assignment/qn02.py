# 2. List & Dictionary: Given a list of numbers, create a  dictionary where each key is a number and the value is its  frequency in the list. 

l=[2,4,5,6,7,4,3,4,5,6,3,4,5,53,4,5,7]
d={}

for num in l: 
    if num in d: 
     d[num]+=1 
    else: 
      d[num]=1 
print(d) 