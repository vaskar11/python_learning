#16. String, Set, & Dictionary: Given a string, create a dictionary where each key is a character, and the value is a set of indices where that character appears in the string.

s="Python programming is fun." 
d={} 
index=0 
for characters in s: 
    if characters  not in d: 
       d[characters]={index,}   
    else: 
       d[characters].add(index) 
       index+=1 
print(d) 