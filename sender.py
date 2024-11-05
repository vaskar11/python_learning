from emp import *
import pickle
f= open("emp.dat", "wb")
while True:
    eno= int(input("Enter your emoloyee number"))
    ename= (input("Enter your emoloyee name"))
    esal= int(input("Enter your emoloyee salary"))
    eaddr= (input("Enter your emoloyee address"))
    e=  Employee(eno, ename, esal, eaddr)
    pickle.dump(e,f)
    option= input("Do you want to serialize more obj?[Yes/No]")
    if option.lower()== "no":
        break
    print("Serialization completed.")
    