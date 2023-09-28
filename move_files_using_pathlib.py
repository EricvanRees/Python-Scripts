import pathlib
import datetime
import shutil


def clean_up_files():

    source = r'C:\Users\mipc\Downloads'

    target = r'C:\Users\mipc\Downloads\old'

    # Create Path objects
    target_dir = pathlib.Path(target)

    source_dir = pathlib.Path(source)

    # Create datetime object for today's date
    today = str(datetime.date.today())

    # Create target directory if necessary
    if target_dir.exists():
        print("target dir already exists")
    else:
        pathlib.Path.mkdir(target_dir)
        print("created new dir")

    # iterdir is pathlib's answer to os.listdir()
    for filename in source_dir.iterdir():

        # check to see last modification date of each file
        modify_timestamp = filename.stat().st_mtime

        modify_date = str(datetime.datetime.fromtimestamp(modify_timestamp))

        # the date information is at the beginning of the string object, which is stored in a new object
        modify_date = modify_date[0:10]

        if modify_date == today:

            # check if there's a file extension to skip folder names
            if pathlib.PurePath(filename).suffix:

                # move file to folder
                shutil.move(filename, target_dir)
                print(f"moved '{filename.parts[-1]}' to {target_dir}.")


clean_up_files()
