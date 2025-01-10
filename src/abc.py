def main():
    # print("hello abc")

    num = float(input("Enter a number: "))
    print("Entered number is", is_num_odd(num))


def is_num_odd(x):
    
    if x <= 0 or int(x) != x:
        return "neither odd nor even"
    elif (x % 2):
        return "odd"
    else:
        return "even"


if __name__ == "__main__":
    main()

