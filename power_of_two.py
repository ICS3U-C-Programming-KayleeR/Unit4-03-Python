#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 11, 11, 2026
# This program raises positive
# whole numbers to the power of 2 using a for loop.


def main():
    # get user number
    user_num = input("Enter a positive whole number: ")
    print()

    # check if user input is an intger
    try:
        user_int = int(user_num)

        # eliminate negative numbers
        if user_int < 0:
            print("Integer inputs must be positive")
        else:
            for counter in range(user_int + 1):
                power_2 = counter**2
                print("{} to the power of 2 is {}".format(counter, power_2))
        print()
    except:
        print("{} is not a positive integer".format(user_num))
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
