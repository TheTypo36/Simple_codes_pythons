#to find the area of the triangle
import math
a=float(raw_input("enter the base of the triangle"))
b=float(raw_input("enter the height of the triangle"))
c=float(raw_input("enter the other side"))
s=(a+b+c)/3
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print "the area of the triangle is:",area
