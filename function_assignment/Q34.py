# 34. Lambda function with map() to convert a list of temperatures from Celsius to Fahrenheit

celsius_to_fahrenheit = lambda lst: list(map(lambda c: (c * 9/5) + 32, lst))
print("Celsius to Fahrenheit:", celsius_to_fahrenheit([0, 25, 30, 100]))