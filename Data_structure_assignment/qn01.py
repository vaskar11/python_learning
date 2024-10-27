# 1. String & List: Given a sentence, split the sentence into words, remove duplicate words (maintaining the order), and return the result as a list

s="Hi my name is Bhaskar Subedi. Hi i love python".split()
final_list=[] 
for word in s: 
    if word in final_list: 
     continue 
    else: 
     final_list.append(word) 

print(final_list) 