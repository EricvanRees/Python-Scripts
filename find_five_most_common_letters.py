"""
The following snippet opens a file folder with text files and reads each file line for line, character for character. All letters are counted, after changing uppercase letters to lowercase letters. Only the five most common letters are printed with their occurances (counts) as a list of tuples.

"""

import os


def count_letters():

    mydict = {}

    dirname = r"c:\Users\mipc\Downloads\files\books"

    for filename in os.listdir(dirname):
        filepath = dirname + '\\' + filename

        if filename[-4:] == '.txt':

            with open(filepath, encoding='utf8') as filedata:
                lines = filedata.readlines()

                for line in lines:
                    if line.startswith(" "):
                        continue
                    else:
                        line = line.split()
                        for word in line:
                            for ch in word:

                                if not ch.isalpha():
                                    continue

                                if ch.isupper():
                                    ch = ch.lower()

                                if ch not in mydict.keys():
                                    mydict[ch] = 1
                                else:
                                    mydict[ch] += 1

    # sort dict by values, use reverse=True to start with highest values
    sorted_tuples = sorted(
        mydict.items(), key=lambda item: item[1], reverse=True)
    # print the five most common letters and their occurances for all files in the directory
    print(sorted_tuples[0:5])


count_letters()
