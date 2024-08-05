#Find CircleArea = 22/7*r*r
def Circle(r):
    area = 22/7*r*r
    return area

r = float(input("Radius :"))

area = Circle(r)
print ("พื้นที่วงกลม : ", str(area))