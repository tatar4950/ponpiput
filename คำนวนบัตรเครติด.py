creaditgard = float(input("Enter your money (0 - 100,000): "))

if 80 <= money <= 100000:
    creaditgard = "platium"
elif money >= 70000-99999:
    creaditgard = "gold"
elif money >= 40000-89999:
    creaditgard = "silver"
elif money >= 100000:
    creaditgard = "youcannotusecreaditgard"

    creaditgard = "Invalid input (money must be between 0 and 100)"

print(f"money: {money}")