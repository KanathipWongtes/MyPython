x = int(input("Enter a number to create its multiplication table: "))
y = 1
while y <= 12:
    z = x * y
    print("%d x %d = %d" % (x, y, z))
    y += 1
