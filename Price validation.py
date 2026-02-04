def validate_price(text: str) -> float:
    """
    This validates a string input to ensure it represents a valid price. The
    function attempts to convert the string input to a float and ensures it
    meets specific business rules. These are the price must be numeric,
    greater than 0, and not exceed 1000.

    Args:
        text (str) - the raw string input representing the price.

    Returns:
        float - the validated price

    Raises:
        ValueError - if the input is empty or whitespace
        ValueError - if the input isn't a number
        ValueError - if the value is <= 0
        ValueError - if the value is > 1000
    """

    # Check 1: Empty or whitespace validation
    if not text or not text.strip():
        raise ValueError("A price is required")
    
    # Check 2: Numeric type validation
    try:
        price = float(text)
    except ValueError:
        # This catches the specific ValueError then re-raises it with a custom message
        raise ValueError("The price must be a number")
    
    # Check 3: Minimum value validation
    if price <= 0:
        raise ValueError("The price must be greater than 0")
    
    # Check 4: Maximum value validation
    if price > 1000:
        raise ValueError("The price must not exeed 1000")
    
    # Finally, return the valid float
    return price

while True:
    user_price = input("Enter a price: ")
    try:
        price = validate_price(user_price)
    except ValueError as e:
        print(f"Error: {e}")
        continue

    print(f"Price accepted: £{price:.2f}")
    break