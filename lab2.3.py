weight = input("กรุณากรอกน้ำหนัก (กิโลกรัม): ")
height = input("กรุณากรอกส่วนสูง (เซนติเมตร): ")

weight = float(weight)
height = float(height) / 100

if weight <= 0 or height <= 0:
    print("กรุณากรอกน้ำหนักและส่วนสูงที่มากกว่า 0")
else:
    # คำนวณ BMI
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    # แสดงผลลัพธ์
    print(f"BMI ของคุณคือ: {bmi}")

    # กำหนดเกณฑ์ของ BMI
    if bmi < 18.50:
        print("อยู่ในเกณฑ์: น้ำหนักน้อย / ผอม (มากกว่าค่ามาตรฐาน)")
    elif 18.50 <= bmi <= 22.90:
        print("อยู่ในเกณฑ์: ปกติ (สุขภาพดี)")
    elif 23.00 <= bmi <= 24.90:
        print("อยู่ในเกณฑ์: ท้วม / โรคอ้วนระดับ 1 (อันตรายระดับ 1)")
    elif 25.00 <= bmi <= 29.90:
        print("อยู่ในเกณฑ์: อ้วน / โรคอ้วนระดับ 2 (อันตรายระดับ 2)")
    else:
        print("อยู่ในเกณฑ์: อ้วนมาก / โรคอ้วนระดับ 3 (อันตรายระดับ 3)")

