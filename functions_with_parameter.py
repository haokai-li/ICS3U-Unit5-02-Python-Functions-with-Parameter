#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about functions with parameter


def calculate_area_triangle(length, height):
    # This function calculate the area of the triangle

    # process
    area = (length * height) / 2

    # output
    print("The area of the triangle is {} cm².".format(area))

    print("\nDone.")


def main():
    # This function just call other functions

    # input
    user_length_string = input("Please enter the base length of a triangle(cm): ")
    user_height_string = input("Please enter the height of a triangle(cm): ")
    print("")

    try:
        user_length_number = float(user_length_string)
        user_height_number = float(user_height_string)

        # call functions
        calculate_area_triangle(user_length_number, user_height_number)

    except Exception:
        # output
        print("You didn't enter an integer.")

        print("\nDone.")


if __name__ == "__main__":
    main()
