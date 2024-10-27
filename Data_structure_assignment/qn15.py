#15. List, Dictionary, & String: Given a list of sentences,create a dictionary where each keyis a unique word and the value is the total number of sentences in which that word appears.

l=["Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."]

d={} 
for sentence in l: 
    words=sentence.lower().replace(".","").replace(",","").split() 
    count_word=[] 
    for word in words: 
        if word not in count_word: 
            if word in d: 
                d[word]+=1 
            else: 
                d[word]=1 
            count_word.append(word) 
 
print(d) 