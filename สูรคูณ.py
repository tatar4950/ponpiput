number = int(input("กรุณากรอกตัวเลขจำนวนเต็ม: "))
print(f"\nตารางสูตรคูณของ {number}")
for i in range(1, 13):  # ปกติสูตรคูณถึง 12
    result = number * i
    print(f"{number} x {i} = {result}")