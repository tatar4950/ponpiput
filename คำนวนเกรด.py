score = float(input("Enter your score (0 - 100): "))

# Check and calculate grade
if 80 <= score <= 80:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "F"
else:
    grade = "Invalid input (score must be between 0 and 100)"

print(f"Score: {score}")
print(f"Grade: {grade}")