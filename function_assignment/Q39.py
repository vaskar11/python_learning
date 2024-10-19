# 39. Function to describe a person with optional keyword arguments (using **kwargs)

def describe_person(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print("Person description:")
describe_person("Bhaskar", age=23, job="Engineer", city="Dubai")
