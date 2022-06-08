#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program generates random numbers using arrays and finds the min.

import random


def find_min(num_array):
    # this function finds the lowest number in the num_array

    min_num = num_array[0]

    for num_check in num_array:
        if num_check < min_num:
            min_num = num_check

    return min_num


def main():
    # this function generates 10 random numbers, calls a function, and outputs the lowest one

    num_array = []

    print("This program generates 10 random numbers and finds the lowest one.\n")

    # process & output
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        num_array.append(random_num)
        print("Random number generated: {}".format(random_num))

    # call function
    min_num = find_min(num_array)

    # output
    print("\nThe lowest number is {}.".format(min_num))

    print("\nDone.")


if __name__ == "__main__":
    main()
