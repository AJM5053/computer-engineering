def read_text_file(path: str) -> str:
    """
    This reads the contents of a text file.

    Args:
        path - where the file is located.

    Returns:
        The file contents as a string.

    Raises:
        ValueError - if file can't be read.
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except OSError as e:
        raise ValueError(f"Couldn't read file {path}") from e

def parse_numbers(text: str) -> list[float]:
    """
    This parses a comma seprated string into a list of floats.

    Args:
        text - comma seperated numeric tokens.

    Returns:
        A list of parsed floats.

    Raises:
        ValueError - if no valid numbers exist or any token is invalid.
    """
    raw_tokens = [t.strip() for t in text.split(",")]
    tokens = [t for t in raw_tokens if t != ""]

    if not tokens:
        raise ValueError("No numbers provided.")
    
    values: list[float] = []
    for t in tokens:
        try:
            values.append(float(t))
        except ValueError as e:
            raise ValueError(f"Invalid number token {t!r}") from e
    
    return values

def median(values: list[float]) -> float:
    if not values:
        raise ValueError("At least one value is required.")
    vals = sorted(values)
    n = len(vals)
    mid = n // 2
    if n % 2 == 1:
        return vals[mid]
    return (vals[mid - 1] + vals[mid]) / 2.0

def summary(values: list[float]) -> dict[str, float]:
    """
    This gives the sum, count, mean, median, min, and max of a list of numbers.

    Args:
        values - a list of floats.

    Returns:
        A dictionary with sum, count, mean, median, min, and max as keys.

    Raises:
        ValueError - if values is empty.
    """
    if not values:
        raise ValueError("At least one value is required.")
    
    total = sum(values)
    count = float(len(values))
    mean = total / count

    return {
        "Sum": total,
        "Count": count,
        "Mean": mean,
        "Median": median(values),
        "Min": min(values),
        "Max": max(values)
    }

def format_summary(stats: dict[str, float]) -> str:
    """
    This formats summary statistics into a display string.
    """
    return (
        f"Sum: {stats["Sum"]:.2f}\n"
        f"Count: {int(stats["Count"])}\n"
        f"Mean: {stats["Mean"]:.2f}\n"
        f"Median: {stats["Median"]:.2f}\n"
        f"Min: {stats["Min"]:.2f}\n"
        f"Max: {stats["Max"]:.2f}"
    )

def main() -> None:
    """
    This orchestrates input, processing and output.
    Allows repeated execution and robust error handling.
    """
    while True:
        while True:
            user_input = input("Enter comma-seperated numbers OR a file path OR quit: ").strip()
            
            if user_input.lower() == "quit":
                print("Quitting...")
                return
            
            try:
                try:
                    text = read_text_file(user_input)
                except ValueError:
                    print("\nNo file with that name exists. Your input will be used instead.")
                    text = user_input
                
                values = parse_numbers(text)
                stats = summary(values)
                print(format_summary(stats))
                break

            except ValueError as e:
                print(f"Error: {e}\n")
        
        while True:
            again = input("Would you like to run again? (y/n): ")

            if again.lower() == "y":
                print()
                break
            elif again.lower() == "n":
                print("\nGoodbye!")
                return
            else:
                print("Please enter y or n.")

if __name__ == "__main__":
    main()