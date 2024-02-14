# Sort-pictures
This python script will take a folder with files (e.g. pictures) and after creating folder for years and month will put each picture in its respective folder based on its creation date

# HOW TO UPLOAD NEW PHOTOS INSIDE THE FOLDER USING CREATION DATE TO DIVIDE IN FOLDERS

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
