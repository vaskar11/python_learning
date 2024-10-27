#35. Tuple, List & Set: Write a Python program that takes a list of tuples, where each tuple  contains a name and an age, and returns a set of names whose age is greater than the  average age of all people in the list.

user_input=eval(input("Enter list of tuple with name and  age: ")) 
s=set() 
for t in user_input: 
   s.add(t[1]) 
average_age=sum(s)/(len(s)) 

set_of_name=set()    
for t in user_input: 
    if t[1]>=average_age: 
       set_of_name.add(t[0]) 
print(set_of_name) 