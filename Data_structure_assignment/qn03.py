# 3. Set & String: Write a Python program that takes two strings  and returns the set of unique characters that appear in both  strings.

s1=input("Enter a first string")
s2=input("Enter a second string")
s=set()
for characters in s1: 
    if characters in s2 and characters not in s : 
     s.add(characters) 
print(s) 
 