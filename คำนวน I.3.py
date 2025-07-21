min_value = None
while True:
    try:
        number = float(input("ป้อนจำนวนจริงบวก: "))
        if number <= 0:
            break
        if min_value is None or number < min_value:
            min_value = number
    except ValueError:
        break

if min_value is not None:
    print("จำนวนจริงบวกที่มีค่าน้อยที่สุดคือ:", min_value)
else:
    print("ไม่มีจำนวนจริงบวกที่รับเข้ามา")