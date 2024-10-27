#31. Tuple, Dictionary, & List: Given a list of tuples, where each tuple contains a  product name and a price, create a dictionary where the keys are product names, and  the values  are the average prices of those products (in case of multiple occurrences).

l=[("shoe Rack",45000),("Washing machine",77000),("TV",110000),("Dish Washer",50000),("shoe Rack",40000),("TV",100000)] 
d={} 
count={} 
for product,price in l: 
    if product in d: 
        d[product]+=price 
        count[product]+=1 
    else: 
        d[product]=price 
        count[product]=1 
 
for product,avg_price in d.items(): 
    d[product]=avg_price/count[product] 
 
print(d) 