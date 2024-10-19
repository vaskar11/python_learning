# 37. Function to print key-value pairs passed as keyword arguments (using **kwargs)

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print("Details:")
print_details(name="Bhaskar", age=23, city="Kathmandu")