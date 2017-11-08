import math
side1=int(input("enter the side1"))
side2=int(input("enter the side12"))
angle1=int(input("enter the angle1"))
side3=math.sqrt((side1**2)+(side2**2)-(2*side1*side2*math.cos(math.radians(angle1))))
print("the third side is",side3)
