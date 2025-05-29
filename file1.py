def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer: "))
        print(f"Factorial of {n} is {factorial(n)}")
    except ValueError as e:
        print(f"Error: {e}")