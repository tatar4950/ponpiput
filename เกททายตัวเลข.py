target = 85
guess_count = 0

while True:
    try:
        guess = int(input("กรุณาทายตัวเลขระหว่าง 0 - 100: "))
        guess_count += 1

        if guess < 0 or guess > 100:
            print("ขอโทษด้วย ตัวเลขไม่อยู่ในช่วงระหว่าง 0-100 กรุณาทายใหม่")
        elif guess < target:
            print("ขอโทษด้วย ตัวเลขมีค่าน้อยเกินไปที่ตั้งไว้ กรุณาทายใหม่")
        elif guess > target:
            print("ขอโทษด้วย ตัวเลขมีค่ามากเกินไปกว่าที่ตั้งไว้ กรุณาทายใหม่")
        else:
            print(f"ยินดีด้วยคุณทายถูก! คุณทายทั้งหมด {guess_count} ครั้ง")
            break
    except ValueError:
        print("กรุณากรอกตัวเลขจำนวนเต็มเท่านั้น")