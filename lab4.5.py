#Function TriangleArea = 1/2*b*h 
def triangle(b,h):
    area = 1/2*b*h
    return area

base = float(input("Input base: "))
height = float(input("Input height: "))

area = triangle(base, height)
print(f"The area of the triangle is: {area}")
