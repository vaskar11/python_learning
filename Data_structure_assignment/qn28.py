#28. List, Dictionary, & Set: Given a list of tuples (name, score), create a dictionary where the keys  are the names, andthe values are the scores, then return a set of names whose  scores are above a certain threshold.

l=[("Ram", 85), ("Shyam", 90), ("Nikita", 78), ("Sita", 78), ("Gita", 90), ("Mita", 76)] 
d={} 
threshold=80 
s=set() 
for t in l: 
    d[t[0]]=t[1] 
for k,v in d.items(): 
    if v>threshold: 
     s.add(k) 
print(s) 