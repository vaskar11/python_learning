#10. String, List, & Dictionary: Given a paragraph, count the frequency of each word (case-insensitive) and return a dictionary where the keys are the words and the values are their frequencies.

paragraph=" Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python is dynamically typed and garbage-collected. "

words=paragraph.lower().split(" ") 
d={} 
for word in words: 
    if word in d: 
        d[word]+=1 
    else: 
        d[word]=1 
 
print(d) 