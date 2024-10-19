# 41. Function to find the maximum value from arguments passed (using *args)

def find_max_in_args(*args):
    return max(args)

print("Max in arguments:", find_max_in_args(10, 20, 30, 5))