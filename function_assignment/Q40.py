# 40. Function to print all positional and keyword arguments (using *args and **kwargs)

def combine_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print("Combine args and kwargs:")
combine_args_kwargs(1, 2, 3, name="Bhaskar", age=23)