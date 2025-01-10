def main():
    # print("hello abc")

    num = float(input("Enter a number: "))
    print("Entered number is", is_num_odd(num))
    print("Is the number a multiple of 3?", is_multiple_of_three(num))


def is_num_odd(x):
    if x <= 0 or int(x) != x:
        return "neither odd nor even"
    elif (x % 2):
        return "odd"
    else:
        return "even"


def is_multiple_of_three(x):
    if x % 3 == 0:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    main()
