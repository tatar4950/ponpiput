if "hour" < 0 or "minute" < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    total_hours = "hour"
    if "minute" > 0:
        total_hours += 1  # เศษของชั่วโมงนับเป็น 1 ชั่วโมง

    if total_hours <= 1:
        cost = 0
    else:
        cost = (total_hours - 1) * 30

    print("ค่าจอดรถคือ",)