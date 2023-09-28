"""This script automates moving files from one folder to another, by tagging the current date to the file name 
and moving the file to a different folder if it has been modified today."""

import os
import datetime
import shutil


def move_files():

    # get current date in datetime object
    today = str(datetime.date.today())

    # set source directory
    directory = r"C:\Users\mipc\Downloads"

    # set target directory
    t_dir = r"C:\Users\mipc\Downloads\working"

    # create datetime objects for all files in dir
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        create_time = os.path.getctime(f)
        create_date = datetime.datetime.fromtimestamp(create_time)

        # check if file date matches today's date and
        # set new filename including today's date for files in dir
        c_date = str(create_date).split()[0]

        if c_date == today:
            file_split = f.split(".")
            if len(file_split) > 1:
                new_filename = file_split[0] + \
                    '-' + c_date + '.' + file_split[1]
                os.rename(f, new_filename)
                # move files to target directory
                shutil.move(new_filename, t_dir)
                print(f"moving {new_filename} to {t_dir}")


move_files()
