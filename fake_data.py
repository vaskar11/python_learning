from random import *
alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits= '0123456789'
cities=['KTM','Pokhara','Hetauda','Dang','Butwal','Kavre','Dolakha']
designation=['Software engineer', 'Senior Software engineer','Team Lead','Project Lead','Manager']

def get_fake_name():
    name= choice(alphabets.upper())
    n= randint(2,9)
    for i in range(n):
        name= name + choice(alphabets)
    return name    

def get_fake_enum():
    enum='e-'
    for i in range(4):
        enum=enum + choice(digits)
    return enum

def get_fake_salary():
    esal= uniform(10000,50000)
    return esal

def get_fake_city():
    city= choice(cities)
    return city

def get_fake_mno():
    mno= choice('9')
    for i in range(9):
        mno= mno + choice(digits)
    return mno

def get_fake_desig():
    desig= choice(designation)
    return desig
for i in range(10):
    print("Employee Records: ")
    print('Name: ',get_fake_name())
    print('City: ',get_fake_city())
    print('Employee number: ',get_fake_enum())
    print('Designation: ',get_fake_desig())
    print('Salary: {:.2f}'.format(get_fake_salary()))
    print('Mobile Number: ',get_fake_mno())
    print()
    print()
