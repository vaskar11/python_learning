#5. String & Dictionary: Given a string, count the occurrences of  each character and return the result as a dictionary. 

s="HEllo People I am Bhaskar Subedi"
new_dict={}
for character in s:
    if character in new_dict: 
     new_dict[character]+=1 
    else: 
     new_dict[character]=1 
print(new_dict) 
