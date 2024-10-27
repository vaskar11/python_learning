#32. Set, Dictionary, & List: Given a list of words, create a dictionary where the key is  the word length, and the value is a set of words of that length.
l=["Apple","orange","Grapes","Mango","papaya","Watermelon","Kiwi"]
d={} 
for words in l: 
    if len(words) not in d: 
       d[len(words)]={words} 
    else: 
       d[len(words)].add(words) 
print(d) 