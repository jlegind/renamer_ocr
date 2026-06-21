# Python program to explain shutil.copyfile() method

# importing os module
import os

# importing shutil module
import shutil

# path
dest_path = r'C:/ocr_orig'

orig_path = r"C:\ocr2\anbefaling_001.jpg"

res = shutil.copyfile(dest_path, orig_path)
