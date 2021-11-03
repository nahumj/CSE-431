#!/usr/bin/env python3
import random
import sys


def main():
    threshold = 100
    max_value = 50

    number_of_values_generator = range(5, 55, 5)

    random.seed(0)

    for number_of_values in number_of_values_generator:
        threshold = (number_of_values * max_value) / 3
        filename = f"input_{number_of_values}.txt"
        with open(filename, "w") as input_file:
            input_file.write(f"{number_of_values} {threshold}\n")
            for _ in range(number_of_values):
                value = round(random.uniform(0, max_value), 4)
                input_file.write(f"{value}\n")


if __name__ == "__main__":
    main()
