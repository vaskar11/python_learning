#12. List & Dictionary: Write a Python program to group a list of words by their  starting letter into a dictionary, where the key is the starting letter and the value is a list of words.

list=["Bhaskar","Bhuwan","Isha","Nikita","Bibek","Dipesh","Chandu","Ayush"]
d={} 
for words in list: 
    first_letter=words[0] 
    if first_letter in d: 
       d[first_letter].append(words) 
    else: 
       d[first_letter]=[] 
       d[first_letter].append(words) 
print(d) 