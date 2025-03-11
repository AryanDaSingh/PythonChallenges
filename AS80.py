import math

def area(r):
    return (math.pi) * (r**2)

def circ(r):
    return 2 * (math.pi) * r

rad = float(input("What is the radius of the circle?    "))
print(str(area(rad)), "is the area of the circle")
print(str(circ(rad)), "is the circumference of the circle")
