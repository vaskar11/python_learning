rec= {}
n= eval(input("enter number of stds: "))
i=1
while i<=n:
    name=input('enter name of std: ')
    marks= int(input('enter marks of std: '))
    rec[name]=marks
    i+=1
print("record of stds are: ")
print(rec)
for k,v in rec.items: #very important 
    print(f"the marks for {k} is {v}")
    

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

#operators in dict
d={100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
e={100:"kabin", 200: "pragyan", 300:"nikita",400:"dipesh"}
print(d==e) #here ordering is not important only key and values are checked

print("kabin" in d) #it only checks the key only not the  values
print(len(d)) # to check length of the dict

print(d.get(100)) #to get the value with associated with the key
print(d.get(700)) #it gives none 
print(d.get(700),"not found! ") # not found is default value if value is not found
print(d.pop(100), " value not found") #returns the information of the value that is removed
print(d.popitem()) #one item is removed randomly
#to print keys:
print(d.keys()) #return the keys only of the dict
for x in d.keys():
    print(x)
    
#to print value:
print(d.values()) #return the values only of the dict
for x in d.values():
    print(x)
    
#gives both keys and values
print(d.items) 
for k,v in d.items:
    print(k,v)
    
e=d.copy() #it clones d in e
d[500]='dipesh'
print(d)
print(e)

print(d.setdefault(500,"dipesh")) #it also says to add dipesh in 500
print(d.setdefault(100,"kabin")) 
print(d) #it will discart the new value

