import math
sides=int(input())
length=int(input())
area=(sides*length**2)/(4*math.tan(math.pi/sides))
print("area:",area)