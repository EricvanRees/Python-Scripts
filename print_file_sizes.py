""" The following Python snippet reads all filenames in a filefolder and lists the individual file sizes in a dictionary. Using the os.stats() function, you can list the file sizes in bytes or megabytes. I used kilobytes (kB) by dividing the bytes value by 1024. This solution is not perfect but you could use this code to improve it yourself if you want to.

Basically, it works like this:

1. Ask the user for a file folder path
2. Create a variable name for each file name
3. Use the os.stat() function to calculate the file sizes
4. Store the filename and file size as key-value pairs in a dictionary
5. Return or print that dictionary

"""

import os


def file_sizes():

    file_sizes = {}

    dirname = input("Please specify directory location: ")

    for filename in os.listdir(dirname):
        filepath = dirname + '\\' + filename
        file_stats = os.stat(filepath)
        file_sizes[filename] = f"{round(file_stats.st_size/1024)} kB"

    print(file_sizes)


file_sizes()
