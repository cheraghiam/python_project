from src.constant import single_digit, teen, tens


def Num2Word(num: int) -> str:
    """Num2 word int number for below 100 numbers

    Args:
        :input user for convert to word 

    Returns:
        : result num to word
    """
    if num in single_digit:
        return single_digit[num]

    if num in teen:
        return teen[num]

    if num in tens:
        return tens[num]

    if num < 100:
        return tens[num // 10 * 10] + " " + single_digit[num % 10]

if __name__ == "__main__":
    print(Num2Word(10))
    print(Num2Word(31))
    print(Num2Word(56))
    print(Num2Word(85))
    print(Num2Word(98))
    