"""Create a text file (using an editor, not necessarily Python) containing two tabseparated
columns, with each column containing a number, for example:

1  6
3  8
2  7
8  9
11  45
88  11
34  13
1  66
45  12
222  5
33  22
11  777

Then use Python to read through the file you’ve created. For each line, multiply each first number by the second, and then sum the results from all the lines. Ignore any line that doesn’t contain two numeric columns."""

import math


def read_file():

    inputFile = r"C:\Users\mipc\Downloads\columns_numbers.txt"

    with open(inputFile, 'r') as filedata:

        lines = filedata.readlines()

        mylist = []

        for line in lines:

            # edit text file to create tuples containing two string values

            line = line.strip()

            line = " ".join(line.split())

            line = line.split()

            tuple_line = tuple(line)

            # convert each string inside each tuple to an integer so you can calculate row products

            tuple_line = tuple(map(int, tuple_line))

            mylist.append(tuple_line)

        print(f"List of tuples: {mylist}")

        # math.prod() calculates the product for each tuple

        tuple_prod = [math.prod(t) for t in mylist]

        print(f"Product of each tuple: {tuple_prod}")

        total = sum(tuple_prod)

        print(f"total of all sums is {total}")


read_file()
