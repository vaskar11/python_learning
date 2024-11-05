# import pickle
# class Employee:
#     def __init__(self, eno, ename, esal, eaddr):
#         self.eno= eno
#         self.ename= ename
#         self.esal= esal
#         self.eaddr= eaddr
#     def display(self):
#         print(f" Eno:{self.eno} \n Ename= {self.ename}\n Esal={self.esal}\n Eadd={self.eaddr}")

# e= Employee('e101','Ram', 20000,'KTM')
# e.display()
# with open("emp.dat",'wb') as f:
#     pickle.dump(e,f)
#     print("picking finished")
    
# with open('emp.dat','rb') as f:
#     obj= pickle.load(f)
#     print("unpickling finished.")
# obj.display()


# import json
# employee={
#     "name":"dipesh",
#     "age":20,
#     "salary":10000,
#     "is_marrid": None
# }
# json_string= json.dumps(employee)
# print(json_string)
# with open('emp.json','w') as f:
#     json.dump(employee,f,indent= 5)
    
    
# import json
# json_string='''{
#      "name": "dipesh",
#      "age": 20,
#      "salary": 10000,
#      "is_married": null
# }'''

# emp_dict= json.loads(json_string)
# print(emp_dict)
# print("Emp Name ",emp_dict['name'])
# print("Emp age ",emp_dict['age'])
# print("Emp salary ",emp_dict['salary'])
# print("Emp is_married ",emp_dict['is_married'])


# import json
# with open('emp.json','r') as f:
#     emp_dict= json.load(f)
# print("Emp Name ",emp_dict['name'])
# print("Emp age ",emp_dict['age'])
# print("Emp salary ",emp_dict['salary'])
# print("Emp is_married ",emp_dict['is_married'])


# import requests
# response= requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
# binfo= response.json()
# value= binfo['bpi']['USD']['rate']
# # print(type(binfo))
# # print(binfo)
# print('1 bitcoin value in dollor: ',value)


# import json
# class Employee:
#     def __init__(self, eno, ename, esal, eaddr):
#         self.eno= eno
#         self.ename= ename
#         self.esal= esal
#         self.eaddr= eaddr
#     def display(self):
#         print(f" Eno:{self.eno} \n Ename= {self.ename}\n Esal={self.esal}\n Eadd={self.eaddr}")
        
# e= Employee('e101','hari', 20000,'KTM')  
# emp_dict= e.__dict__
# # emp_dict= {'eno':e.eno, "ename":e.ename, "esal":e.esal, "eaddr": e.eaddr}
# with open("emp.json",'w') as f:
#     json.dump(emp_dict, f, indent=4)
    
# with open("emp.json",'r') as f:
#     edict=json.load(f)
# print(edict)


# import jsonpickle
# class Employee:
#     def __init__(self, eno, ename, esal, eaddr,isMarried):
#         self.eno= eno
#         self.ename= ename
#         self.esal= esal
#         self.eaddr= eaddr
#         self.isMarried=isMarried
#     def display(self):
#         print(f" Eno:{self.eno} \n Ename= {self.ename}\n Esal={self.esal}\n Eadd={self.eaddr}\nisMarried={self.isMarried}")

# e= Employee(101,"Bhaskar",50000,'Dang',None)
# #serialization to string:
# json_string= jsonpickle.encode(e)
# # print(json_string)

# #seriaization to file:
# with open("emp.json",'w') as f:
#     f.write(json_string)


from pyaml import yaml

employee={
     "name": "dipesh",
     "age": 20,
     "salary": 10000,
     "is_married": None
}
# yaml_string= yaml.dump(employee)
# print(yaml_string)
# with open("emp.json",'w') as f:
#     yaml.dump(employee,f)
    
with open('emp.json','r') as f:
    a= yaml.safe_load(f)
print(a)