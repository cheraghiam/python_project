def happy_number(n: int) -> bool:
    """Check if a number is a happy number.

    Example:
        happy_number(7)
        # Output: True

    Returns:
        True if the number is happy, False otherwise.
    """
    seen_number = set()
    while (n != 1) and (n not in seen_number):
        seen_number.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    if n == 1:
        return True
    return False


def input_user_number() -> int:
    """Prompt the user to enter a number.

    Returns:
        The number entered by the user.
    """
    user_number = input("Enter your number: ")
    try:
        return int(user_number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        input_user_number()


if __name__ == "__main__":
    user_number = input_user_number()
    print(f"your number {user_number} is happy: {happy_number(user_number)}")
