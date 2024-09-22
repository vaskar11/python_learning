words_upto_19 = [
    '',"one", "two", "three", "four", "five", "six", "seven", 
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", 
    "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
    "nineteen"
]
words_for_teen = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']

n= int(input("enter a number: "))
if n==0:
    output ="zero"
elif n<=19:
    output= words_upto_19[n]
elif n<=99:
    output= words_for_teen[n//10] + " " + words_upto_19[n%10]
    
print(output)