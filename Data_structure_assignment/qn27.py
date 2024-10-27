#27. String, List, & Dictionary: Write a program that takes a string and returns a dictionary  where the keys are the first characters of words in the string, and the values are lists of words that start with that character.

user_input=input("Enter a string: ") 
d={} 
l=user_input.split(" ") 
for word in l: 
    first_char=word[0] 
    if first_char in d: 
        d[first_char].append(word) 
    else: 
        d[first_char]=[word] 
print(d) 