"""
The following Python snippets contain two functions. The first one, find_longest_word, takes a filename as an argument and returns the longest word found in the file. The second function, find- _all_longest_words, takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file.

When calling the first function in the second function, it is important to note that you need to set a variable that contains the return value of that function, otherwise you cannot use it within that second function. In this case, the variable longest_word contains the return value of the first function (which also called longest_word). You need this variable to populate the dictionary that contains the different filenames (as keys) and longest words within that file (dictionary values).

I received many errors when reading the different .txt files, so I put encoding info (UTF-8) when opening them. This solved these errors. Also, I limited the amount of input files, using only a few .txt files that contain entire books. The example code uses a dictionary comprehension, but I chose to use simple for loops. Note that you only need to call the second function with a directory location to have the first one automatically called from within that function.

find_longest_word takes a filename as an argument and returns the longest word found in the file. The second function, find-_all_longest_words, takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file.

"""

import os


def find_longest_word(filename):

    longest_word = ''

    with open(filename, encoding='utf8') as f:

        lines = [line.rstrip() for line in f]

        for line in lines:
            line = line.split(" ")

            for word in line:

                if len(word) > len(longest_word):
                    longest_word = word

    return longest_word


def find_all_longest_words(dirname):

    mydict = {}

    for filename in os.listdir(dirname):
        filepath = dirname + '\\' + filename
        if filename.endswith(".txt"):

            longest_word = find_longest_word(filepath)
            mydict[filename] = longest_word

    print(mydict)


dirname = r"c:\Users\mipc\Downloads\files\books"

find_all_longest_words(dirname)
