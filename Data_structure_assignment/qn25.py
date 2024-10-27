#25. Set, List, & String: Given two lists of strings, return a list of strings that are in both  lists, but only include those that have more than 3 vowels.

l1 = ["hello", "python", "programming", "and", "programmers","in","this","example"] 
l2=["hello", "java", "programming", "and", "developers","in","that","example"] 
vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') 
common_list = [] 
for element in l1: 
    if element in l2: 
      count=0 
for i in range(len(element)): 
    if element[i] in vowel: 
       count+=1 
if count >= 3: 
     common_list.append(element) 
print(common_list) 