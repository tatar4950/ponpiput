for i in range(5):
    num = int(input(f"ป้อนตัวเลขจำนวนเต็มตัวที่ {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("ผลรวมของตัวเลขทั้งหมดคือ:", total)
print("ค่าเฉลี่ยของตัวเลขคือ:", average)