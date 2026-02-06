while True:
    try:
        age = int(input("Enter your age: "))
        if 0 < age <= 120:
            print(f"Your age is {age}")
            break
        else:
            print("Your age must be between 1 and 120. Please try again")
    except ValueError:
        print("Invalid input. Please enter a number")

print()
inventory = []

milk = {
    "Name":"Milk",
    "Price":1.20,
    "Stock_Level":25
}

apples = {
    "Name":"Apples",
    "Price":1.55,
    "Stock_Level":0
}

beans = {
    "Name":"Beans",
    "Price":0.82,
    "Stock_Level":37
}

inventory.append(milk)
inventory.append(apples)
inventory.append(beans)

for item in inventory:
    status = "In Stock" if item["Stock_Level"] > 0 else "Out of Stock"
    print(f"Product: {item["Name"]} | Price: £{item["Price"]:.2f} | Status: {status}")

print()
def get_vat(price: float) -> float:
    """
    This calculates the VAT at 20% for a given price

    Args:
        price (float) - the input which represents the price

    Returns:
        float - the calculated VAT for that price
    """
    return price * 0.2

price = float(input("Enter a price: "))
vat = get_vat(price)
print(f"The VAT is {vat:.2f}")