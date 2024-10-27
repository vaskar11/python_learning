#22. String & Tuple: Write a program that takes a string,creates a tuple of each word in the  string, and sorts the tuple in reverse alphabetical order.

user_input=input("Enter a string: ") 
t=tuple(user_input) 
sorted_tuple=tuple(sorted(t,reverse=True)) 
print(sorted_tuple) 