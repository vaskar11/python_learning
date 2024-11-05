import pickle
f= open("emp.dat","rb")
print("Deserialiation started")
while True:
    try:
        obj= pickle.load(f,)
        obj.display()
        
    except EOFError:
        break
        
        