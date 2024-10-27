#30. String, Set, & List: Given a string of space-separated words, return a sorted list of  words that appear more than once, without duplicates.

string="This ia all about programming and about programmers. This code is a part of data structure questions and all these data types are very important." 
l=string.split(" ") 
l1=[] 
for words in l: 
    count=0 
    for again_word in l: 
        if words==again_word: 
           count+=1 
    if count>1: 
        l1.append(words) 

sorted_list=sorted(set(l1)) 
print(sorted_list) 