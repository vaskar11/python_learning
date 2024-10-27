#4. Tuple & List: Given a list of tuples where each tuple contains  two numbers, return a new list containing the product of the  two numbers in each tuple.

l=[(1,2),(4,5),(6,7),(4,0),(1,1)]
l1=[]
for tuples in l:
    a,b=(tuples)
    product=a*b
    l1.append(product)
print(l1)
