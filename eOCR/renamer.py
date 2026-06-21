# import uuid
# from os import listdir,rename
# from shutil import copy
#
# myPath = "C:/Users/Kris/memes/"
# testPath = "C:/Users/Kris/testOCR/"
# filepaths = [myPath+f for f in listdir(myPath)]
# print('----',filepaths)
#
# paths = filepaths[0:5]
#
# print(paths)
#
# def renamer(pathList):
#     print('IN pathlist()()()')
#     for j in pathList:
#         print(j, uuid.uuid4(), testPath+str(uuid.uuid4())+".jpeg")
#         copy(j, testPath+str(uuid.uuid4())+".jpeg")
#
# renamer(paths)

# Write text to a file

import shutil
# import easyocr

# # Using raw strings (recommended for Windows paths)
# shutil.move(r'C:\tempo\file.txt', r'C:\backup\file.txt')

# Using forward slashes (also works on Windows)
shutil.move('C:/tempo/zyzz_statue.png', 'C:/backup/')

# Using pathlib (most robust)
# from pathlib import Path
#
# source = Path('C:/temp/file.txt')
# destination = Path('D:/backup/file.txt')
# shutil.move(source, destination)