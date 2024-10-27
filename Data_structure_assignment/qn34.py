#34. Dictionary, List, & String: Given a string of sentences,create a dictionary where the keys  are the words (case-insensitive) and the values are lists of sentences in which each word appears.

string="Cats are pet animals. Also the dog is pet. Both dog and cat are beautiful." 
d={} 
l=string.lower().replace(".","").split(" ") 
sentences=string.split(".") 
for sentence in sentences: 
    words = sentence.lower().replace(".", "").split() 
    for word in words: 
       if word not in d: 
           d[word] = [] 
    d[word].append(sentence) 
print(d)   