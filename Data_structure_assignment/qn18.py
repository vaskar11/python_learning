#18. String, List, & Set: Given a string, find all the unique words (case-insensitive) that appear in the string and return them as a sorted list.

string="Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."
l=string.lower().replace(".","").split(" ") 
s=set(l) 
l=sorted(s) 
print(l) 