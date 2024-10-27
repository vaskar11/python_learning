#26. Tuple, List, & Set: Given a list of tuples, each containing two integers, create a set of sums  of all the pairs, and return the result as a sorted list.

l = [(7,9),(5,4),(9,2),(7,8),(6,10)] 
s=set() 
for t in l: 
     s.add(sum(t)) 
result=sorted(s) 
print(result) 