#!/usr/bin/python3
import sys


def factorize(value):
    num1 = 2
    while (value % num1):
        if (num1 <= value):
            num1 += 1

    num2 = value // num1
    return (num2, num1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

file_name = sys.argv[1]

file = open(file_name, 'r')
lines = file.readlines()

for line in lines:
    value = int(line.rstrip())
    num2, num1 = factorize(value)
    print(f"{value} = {num2} * {num1}")
