#29. Tuple, List & Set: Write a Python program that takes am list of tuples, where each tuple  contains a name and an age,and returns a set of unique ages, and creates a new list of tuples with the names of people who are older than 30.

user_input=eval(input("Enter list of tuple with name and age: ")) 
unique_age=set() 
for t in user_input: 
    unique_age.add(t[1]) 
older_Age=30 
older_than_30=[] 
for t in user_input: 
    if t[1]>30: 
       older_than_30.append(t) 
print(unique_age) 
print(older_than_30) 


