#17. List, Set & Tuple: Write a Python program to remove duplicates from a list of tuples (each tuple contains two elements), and return the result as a set of tuples.

l=[("Bhaskar","SUbedi"),(2,5),(7,3),(4,8),(2,5),("Bhaskar","Subedi")] 
final_set=set() 
for elements in l: 
     final_set.add(elements) 
print(final_set) 