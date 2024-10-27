#19. Set & Dictionary: Given a dictionary of words as keys and their definitions as values, return a set containing all the words whose definitions contain a specific keyword.

d={"Absence":"The lack or unavailability of something or someone.","Approval":"Having a positive opinion of something or someone.","Answer":"The response or receipt to a phone call, question, or letter.","Attention":"Noticing or recognizing something of interest.","Amount":"A mass or a collection of something","Borrow":"To take something with the intention of returning it after a period of time."} 
s=set() 
user_input=input("Enter a keyword: ") 
for k,v in d.items(): 
    if user_input in v: 
     s.add(k) 
print(s) 