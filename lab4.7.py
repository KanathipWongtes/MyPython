#BMI Function SUpaNega BMI = W(kg)/(H/100)**2
def bmi(w, h):
    Urbmi = w / (h / 100) ** 2
    return Urbmi

w = float(input("Your Weight (kg): "))
h = float(input("Your Height (cm): "))

Urbmi = bmi(w, h)

print("BMI ของคุณคือ: %.2f" % Urbmi)

if Urbmi < 18.50:
    print("อยู่ในเกณฑ์: น้ำหนักน้อย / ผอม (มากกว่าค่ามาตรฐาน)")
elif 18.50 <= Urbmi <= 22.90:
    print("อยู่ในเกณฑ์: ปกติ (สุขภาพดี)")
elif 23.00 <= Urbmi <= 24.90:
    print("อยู่ในเกณฑ์: ท้วม / โรคอ้วนระดับ 1 (อันตรายระดับ 1)")
elif 25.00 <= Urbmi <= 29.90:
    print("อยู่ในเกณฑ์: อ้วน / โรคอ้วนระดับ 2 (อันตรายระดับ 2)")
else:
    print("อยู่ในเกณฑ์: อ้วนมาก / โรคอ้วนระดับ 3 (อันตรายระดับ 3)")
