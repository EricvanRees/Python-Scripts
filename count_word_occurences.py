"""
The following snippet lets the user input a filepath for a .txt file, as well as an input string with multiple words to count inside that file (separated by a space). The code counts all word occurances of given by the user and outputs a dictionary with the words as keys and word counts as values.

The code populates an empty dictionary as it reads the file line by line, word for word. If there’s a match with the input words from the user, a dictionary key is created with a value of one, and incremented with each new occurance. The first for loop sets all user input words as dictionary keys and values. This means that in case there’s no match, it is still part of the dictionary returned to the user with a value of zero.

When entering the filepath to the .txt file of your choice, do not use commas as Python will convert the input to a string immediately. 

The code has two for loops: one for setting key values for the user input words, so that words with a count of zero are also returned to the user after the second for loop. This loop counts the occurrences of the words entered by the user inside the .txt file.

"""

import os


def count_words():

    inputFile = input("Please enter the textfile's path to analyze: ")

    words_to_count = input("Please enter the words you want to count: ")

    count_list = words_to_count.split(" ")

    mydict = {}

    with open(inputFile, encoding='utf8') as filedata:
        lines = filedata.readlines()

        for word in count_list:
            mydict[word] = 0

        for line in lines:
            for word in line.split():

                if word in count_list:
                    if word in mydict.keys():
                        mydict[word] += 1
                    elif word not in mydict.keys():
                        mydict[word] = 1

        print(mydict)


count_words()
