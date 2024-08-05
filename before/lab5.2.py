def sum(p):
    total = 0
    for i in range(p):
        q = int(input(f"กรอกจำนวนสินค้า {i + 1}: "))
        price = float(input(f"กรอกราคาสินค้า {i + 1}: "))
        total += q * price
    return total

def vat(total):
    return total * 7 / 100

def maintotal(total, vat):
    return total + vat

def caltotalandvat(p):
    total = sum(p)
    vat_amount = vat(total)
    total_with_vat = maintotal(total, vat_amount)
    return total, vat_amount, total_with_vat

def main():
    items = int(input("กรุณากรอกรายการสินค้า: "))
    total, vat_amount, total_with_vat = caltotalandvat(items)
    
    print(f"ราคารวม: {total:.2f} บาท")
    print(f"ภาษีมูลค่าเพิ่ม (7%): {vat_amount:.2f} บาท")
    print(f"ราคารวมทั้งสิ้น: {total_with_vat:.2f} บาท")
    
    cash = float(input("กรุณากรอกจำนวนเงินที่ลูกค้าจ่าย: "))
    change = cash - total_with_vat

    if change>0:
        print(f"เงินทอน: {change:.2f} บาท")

    if change<0:
        print("not enough money!!")

main()
