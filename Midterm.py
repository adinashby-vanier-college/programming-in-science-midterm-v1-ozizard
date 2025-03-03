import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = round(math.pi * radius ** 2, 2)
    return area

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    for i in range (n):
        if n < 4:
            return "The triangle height should be at least 4."
        if i == n+1 or i == 5 or i == 4:
            result += "*" * (n-i)
            result += "\n"
        return result.rstrip()
        if i < (n-1):
            space = " " * (n-i)
            result += "*" + space + "*" + "\n"
        return result.rstrip()
    

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    if n < 3:
        return "The pyramid height should be at least 3."
    else:
        for i in range (n,0,-1):
            space = " " * (n-i)
            stars = "*" * (2 * i -1)
            result += space + stars + "\n"
        return result.rstrip()
# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()