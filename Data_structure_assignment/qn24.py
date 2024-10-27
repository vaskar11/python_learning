#24. String, Tuple, & Dictionary: Write a Python program that takes a string and returns a  dictionary where the keys are words and the values are tuples, with the first element asthe  length of the word and the second as the count of vowels in the word.

user_input=input("Enter a string: ") 
d={} 
vowel=('a','e','i','o','u','A','E','I','O','U') 
words=user_input.split(" ") 
for word in words: 
     count=0 
for char in word: 
    if char in vowel: 
       count+=1 
d[word]=(len(word),count) 
print(d) 