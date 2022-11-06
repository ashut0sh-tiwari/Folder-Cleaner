"""FOLDER CLEANER TO MOVE SIMILAR TYPE OF FILES INTO ONE FOLDER"""

# importing os to use os module
import os

#function to create a folder if not exist
def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
#fuction to move files into a folder
def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

#variable to store all the files in the folder using listdir function
files = os.listdir()
#excluding main program file from files usinf remove function
files.remove("folder cleaner.py")

#creating folders using function
createFolder('Images')
createFolder('Media')
createFolder('Docs')
createFolder('Others')

# variables to list similar type of files 

imgExt = [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff" ]

mediaExt = [".3gp2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv", ".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl" ]

docExt = [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd", ".ods", ".xls", ".xlsm", ".xlsx", ".key", ".odp", ".pps", ".ppt",".pptx"]

#variables to store similar type of files
#os.path.splitext function is used to get the desired extentions

images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExt) and (ext not in imgExt) and (ext not in docExt) and os.path.isfile(file):
        others.append(file)

#moving files into folder using function
move("Images", images)
move("Media", medias)
move("Docs", docs)
move("Others", others)
