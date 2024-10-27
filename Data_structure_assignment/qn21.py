#21. List, Set & Tuple: Given a list of tuples, where each tuple contains two  integers, return a list of tuples where the sum of the integers in each tuple is unique.

l = [(7,9),(5,4),(9,2),(7,8),(6,10)] 
sum_of_tuple=[] 
duplicate_sum=set() 
for t in l: 
    s=sum(t) 
    if s not in duplicate_sum: 
       sum_of_tuple.append(t) 
duplicate_sum.add(s) 
print(sum_of_tuple) 