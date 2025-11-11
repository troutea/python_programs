def check_even_odd():
    """
    Check if a positive integer is even or odd

    Args:
      x(int): A positive integer
    :return:
    str: "Even if the neumber is even "ODD IF THE NUMBER IS ODD
    """


# Test cases
test_numbers = [1, 2, 3, 4, 5, 10, 15, 100, 101]

print("Testing the function:")
for num in test_numbers:
    result = check_even_odd(num)
    print(f"{num} is {result}")
