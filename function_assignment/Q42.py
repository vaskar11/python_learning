# 42. Recursive function to sum all numbers passed as arguments, including nested tuples/lists

def sum_all_recursive(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (list, tuple)):
            total += sum_all_recursive(*arg)
        else:
            total += arg
    return total

print("Recursive sum:", sum_all_recursive(1, 2, [3, 4], (5, 6)))