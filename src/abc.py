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

def get_square(x):
    return x**2

def get_exponent(x, exponent):
    return x**exponent

def get_exponentWithFunction(x, exponent):
    return pow(x, exponent)

if __name__ == "__main__":
    main()

