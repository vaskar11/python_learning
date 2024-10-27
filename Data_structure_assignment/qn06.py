#6. List & Set: Write a Python program to find the common elements between two lists using a set for efficiency.

l1=[1,4,6,8,20,44,5,7,'Bhaskar',8,33,56,87,35,22]
l2=[3,55,7,9,7,2,1,45,67,34,33,35,"Bhaskar",4,6,1,]
s1=set(l1) 
s2=set(l2) 
common_element=s1.intersection(s2) 
print(common_element) 