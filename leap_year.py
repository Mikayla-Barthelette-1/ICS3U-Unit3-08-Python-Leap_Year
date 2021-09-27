#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will see if a year is a leap year


def main():
    # this function determines if the year is a leap year

    # input
    user_input = input("Please enter the year: ")

    # process & output
    try:
        year_entered = int(user_input)
        if year_entered % 4 == 0:
            if year_entered % 100 == 0:
                if year_entered % 400 == 0:
                    print("{0} is definitely a leap year!".format(year_entered))
                else:
                    print("{0} is not a leap year.".format(year_entered))
            else:
                print("{0} is not a leap year.".format(year_entered))
        else:
            print("{0} is not a leap year.".format(year_entered))
    except Exception:
        print("Invalid input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
