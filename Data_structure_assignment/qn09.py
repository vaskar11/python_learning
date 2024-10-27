#9. Set & Dictionary: Write a Python program that checks if a dictionary has all unique values using a set.

d={100:"Bhaskar",700:"Dipesh",300:"Kabin", 200:"Biplov",500:"Ayush"} 
s=set(d.values()) 
if (len(s))==len(d): 
    print("Dictionary contains all unique element.") 
else: 
    print("Dictionary contains duplicate values.") 