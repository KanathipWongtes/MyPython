score =input("ใส่คะแนน : ")
if score.isnumeric():
        if 80 <= score <=100:
            print("เกรด A")
        elif 70 <= score <= 79:
            print("เกรด B")
        elif 60 <= score <= 69:
            print("เกรด C")
        elif 50 <= score <= 59:
                print("เกรด D")if 0 <= score <= 100:
        elif 0 <= score <= 49:
                print("เกรด F")
        else:
            print("กรุณากรอกข้อมูล 0-100")
else:
    print("กรุณากรอกข้อมูล 1-100")
    
