def main():
    # print("hello abc")

    num = float(input("Enter a number: "))
    print("Entered number is", is_num_odd(num))
    print("Is the number a multiple of 3?", is_multiple_of_three(num))


def is_num_odd(x):
    """
    Check if a number is odd or even or neither.

    Args:
        x (float): The number to check.

    Returns:
        str: "odd" if the number is a odd, "even" if the number is even, otherwise "neither odd nor even".
    """
    if x <= 0 or int(x) != x:
        return "neither odd nor even"
    elif (x % 2):
        return "odd"
    else:
        return "even"


def is_multiple_of_three(x):
    """
    Check if a number is a multiple of three.

    Args:
        x (int): The number to check.

    Returns:
        str: "yes" if the number is a multiple of three, otherwise "no".
    """
    if x % 3 == 0:
        return "yes"
    else:
        return "no"


def reverse_string(var):
    """
    Reverses the given string.

    Args:
        var (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(var, str):
        raise ValueError("Input must be a string")
    return var[::-1]

def square_num(x):
    """
    Returns square of a number.

    Args:
        x (float): The number to square.

    Returns:
        float: the number squared.
    """
    return x * x


if __name__ == "__main__":
    main()
