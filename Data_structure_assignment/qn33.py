#33. List, Set, & String: Given a list of strings, create a set containing all unique characters across all strings, then return a list of these characters sorted alphabetically.

l=["Hello","Python","Programmers","This","is","a","python","tutorial","assignment."] 
unique=set() 
for string in l: 
     unique.update(string) 
sorted_list=sorted(unique) 
print(sorted_list) 