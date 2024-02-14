"""
HOW TO UPLOAD NEW PHOTOS INSIDE THE FOLDER USING CREATION DATE TO DIVIDE IN FOLDERS
-----------------------------------------------------------------------------------

This python file and the gallery folder (with pictures) should be inside the same directory/folder.
Open this same directory/folder with VSCode.

If it's the first time running this file (so there aren not year folders yet), the explorer should look like this:

E.G.
-DIRECTORY
    -gallery
        -image1
        -image2
        -image3
        -etc...
    -sort_pictures.py

All is needed is the gallery folder with all the images and by just running this file and all the pictures will be sorted by year and month in thei respective folders.

-----------------------------------------------------------------------------------

If it's NOT the first time running this file, meaning that there are already some years folder, the explorer should look like this:

E.G.
-DIRECTORY
    -gallery
        -2020
            -Jan
                -image1
            -Feb
                -image2
        -2021
            -Sep
                -image3
            Nov:
                -image4
        -etc...
        -image5
        -image6
        -etc...
    -sort_pictures.py

All is need is the gallery folder with both the old years folder and the new images and all the new pictures will be sorted based on their creation date
"""


import os
import shutil
import datetime
from datetime import date

directory = 'gallery'

def creation_date(path) -> date:
    """This function return the creation date of a file
    :param path: the path to the file
    :return the date as datetime.date
    """
    stat = os.stat(path)
    bd_time = stat.st_birthtime

    return datetime.datetime.fromtimestamp(bd_time)


# iterate through all file of directory "gallery"
for filename in os.listdir(directory):

    f = os.path.join(directory, filename)
    photo_date = creation_date(f)

    # if the path is a file (not DS_store file) check directories
    if os.path.isfile(f) and filename != ".DS_Store":
        
        year_dir = os.path.join(directory, str(photo_date.year))
        month_dir = os.path.join(year_dir, str(photo_date.strftime("%b")))

        
        # if there is no year folder yet, create it
        if not os.path.isdir(year_dir):
            # create year folder
            os.makedirs(year_dir)

        # create new location for file
        new_loc = os.path.join(month_dir, filename)

        # if there is no month folder yet, create it
        if not os.path.isdir(month_dir):
                # create month folder
                os.makedirs(month_dir)
                shutil.move(f, new_loc)
        else:
                # move file to new folder
                shutil.move(f, new_loc)

        



