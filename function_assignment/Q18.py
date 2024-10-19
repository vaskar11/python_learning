# 18. Function to calculate the area of a shape

import math

def calculate_area(shape, dimension):
    if shape == "circle":
        radius = dimension[0]
        return math.pi * radius ** 2
    elif shape == "square":
        side = dimension[0]
        return side ** 2
    elif shape == "rectangle":
        length, width = dimension
        return length * width
    else:
        return "Invalid shape"

print(calculate_area('rectangle',[4,5]))