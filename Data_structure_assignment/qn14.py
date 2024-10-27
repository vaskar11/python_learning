#14. Set & List: Write a Python program that removes all elements from a list that appear more than once,  preserving the original order.

l=l=['P','y','t','h','o','n','P','r','o','g','r','a','m','m','i','n','g'] 
s=set() 
dup=set() 
final_list=[] 
for elements in l: 
    if elements in s: 
        dup.add(elements) 
    else: 
       s.add(elements) 

for elements in l: 
    if elements not in dup: 
        final_list.append(elements) 
print(final_list) 