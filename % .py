def calculate_discounted_price(price, discount):
    if 0 <= discount <= 100:
        discounted_price = price - (price * discount / 100)
        return discounted_price
    else:
        return "Invalid discount percentage. Must be between 0 and 100."

original_price = 1000
discount_percent = 20

final_price = calculate_discounted_price(original_price, discount_percent)
print("Final price after discount:", final_price)