import numpy as np


def main():
    # print("hello abc")

    num = float(input("Enter a number: "))
    print("Entered number is", is_num_odd(num))
    # def_array = np.array([True, False, True, True])
    def_array = np.array([True, True, True, True])
    print(hello_bye(def_array))


def is_num_odd(x):
    
    if x <= 0 or int(x) != x:
        return "neither odd nor even"
    elif (x % 2):
        return "odd"
    else:
        return "even"

def hello_bye(def_array):

    if np.all(def_array):
        return "hello"
    else:
        return "bye"

if __name__ == "__main__":
    main()

