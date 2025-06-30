Chestsizet = int(input("Enter your Chestsizet (0 - 100): "))

if 80 <= Chestsizet <= 40:
    Chestsizet = "xl"
elif Chestsizet >= 40:
    Yourpolosuitissize = "l"
elif Chestsizet >= 38:
    Yourpolosuitissize = "m"
elif Chestsizet >= 36:
    Yourpolosuitissize = "s"
elif Chestsizet >= 34:
    Yourpolosuitissize = "xs"
else:
    Yourpolosuitissize = "Invalid input (Chestsizet must be between 0 and 100)"

# Display result
print(f"Chestsizet: {Chestsizet}")