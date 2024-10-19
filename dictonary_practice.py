# rec= {}
# n= eval(input("enter number of stds: "))
# i=1
# while i<=n:
#     name=input('enter name of std: ')
#     marks= int(input('enter marks of std: '))
#     rec[name]=marks
#     i+=1
# print("record of stds are: ")
# print(rec)
# for k,v in rec.items: #very important 
#     print(f"the marks for {k} is {v}")
    

# #updating a dict
# d={100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
# print(d)
# print[100]="bhaskar"
# print(d)
# del d[400], d[200]
# print(d) 
# d.clear()
# print(d)
# del d[300] #ERROR as dict is deleted

# #operators in dict
# d={100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
# e={100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
# print(d==e) #here ordering is not important only key and values are checked

# print("kabin" in d) #it only checks the key only not the  values
# print(len(d)) # to check length of the dict

# print(d.get(100)) #to get the value with associated with the key
# print(d.get(700)) #it gives none 
# print(d.get(700),"not found! ") # not found is default value if value is not found
# print(d.pop(100), " value not found") #returns the information of the value that is removed
# print(d.popitem()) #one item is removed randomly
# #to print keys:
# print(d.keys()) #return the keys only of the dict
# for x in d.keys():
#     print(x)
    
# #to print value:
# print(d.values()) #return the values only of the dict
# for x in d.values():
#     print(x)
    
# #gives both keys and values
# print(d.items) 
# for k,v in d.items:
#     print(k,v)
    
# e=d.copy() #it clones d in e
# d[500]='dipesh'
# print(d)
# print(e)

# print(d.setdefault(500,"dipesh")) #it also says to add dipesh in 500
# print(d.setdefault(100,"kabin")) 
# print(d) #it will discart the new value



# dict practice

# d={100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
# d[500]= 'bhaskar'
# value= d[100]
# print(value)
# my_dict= {100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
# for key, value in my_dict.items():
#     print(key, value)

# d={100:"Bhaskar",200:"Dipesh",300:"Isha",400:"Kabin"}
# (d.setdefault(100,"Angry")) 
# print(d) 
# d={100:"Bhaskar",200:"Dipesh",300:"Isha",400:"Kabin",}
# (d.setdefault(600,"Angry")) 
# print(d) 

# elements = [1, 2, 2, 3, 3, 3,3]
# count_dict = {}
# for elem in elements:
#     count_dict[elem] = count_dict.get(elem, 0) + 1
# print(count_dict)

# list=["Bhaskar", "Biplov","Ankit","Ankrit","Bhuwan","Ayush"]
# d={} 
# for words in list: 
#     first_letter=words[0] 
#     if first_letter in d: 
#       d[first_letter].append(words) 
#     else: 
#       d[first_letter]=[] 
#       d[first_letter].append(words) 

# print(d) 

# d1={100:"Bhaskar",200:"Dipesh",300:"Isha",400:"Kabin"}
# d2={500: 'Prakash', 900: 'Hira', 300: 'Pant', 200: 'buddha'} 
# common_dict={} 
# for k,v in d1.items(): 
#    common_dict[k]=v 
# for k,v in d2.items(): 
#     if k in common_dict: 
#        common_dict[k]+=v 
#     else: 
#        common_dict[k]=v 
# print(common_dict) 

# def case1(): print("Case 1")
# def case2(): print("Case 2")
# switch = {
#     'a': case1,
#     'b': case2
# }
# switch.get('a', lambda: None)()

# nested_dict = {'a': {'b': {'c': 1}}}
# value = nested_dict['a']['b']['c']
# print(value)

#converting it into tuples
l1=[2,4] 
l2=[1,3] 
l3=[6,8] 
l4=[5,7] 
# d={l1:"First two even",l2:"First two odd",l3:"Second two even",l4:"Second two odd"} 
# print(d) 
 
d={tuple(l1):"First two even",tuple(l2):"First two odd",tuple(l3):"Second two even",tuple(l4):"Second two odd"} 
print(d) 