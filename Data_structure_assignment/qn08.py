#8. List, Tuple, & Set: Given a list of tuples (where each tuple contains numbers),  create a set containing the unique elements that appear across all the tuples.

l=[(1,3),(2,5),(3,4),(7,2)]

s=set()
for item in l:
    for x in item:
        s.add(x)
print(s)