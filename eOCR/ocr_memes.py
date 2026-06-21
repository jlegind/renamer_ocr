import sys
from pathlib import Path
import hashlib
import easyocr
from os import listdir,rename
from PIL import Image
import ordered_set
import os

myPath = Path('C:\\', 'Users', 'Kris', 'Pictures', 'memes_OCR') # creating a valid path
myPath = os.path.join(myPath, '', '') # Adding trailing backslash
print('listdirrrrr', listdir(myPath))

filepaths = [myPath+f for f in listdir(myPath)]
print(filepaths)
# We need to ID the img text.
# If text: Rename file with text .jpeg | rename with hash of orig ending in .jpeg
# sys.exit()

def splitter(n, string_, separator='_'):
    #Splits a string into a list of n pieces
    pieces = string_.split()
    return (separator.join(pieces[i:i+n]) for i in range(0, len(pieces), n))
def conc_list(the_list, separator='_', maxTokens=5):
# Joins list into string of max token size
#     sizedList = the_list[0:maxTokens+1]
    print("orig LIST ;;;", the_list)
    concedList = [i.replace(' ', '_') for i in the_list]
    print("SIXED LIst===", concedList)
    joinedString = '_'.join(concedList)
    print('joinedDDDD', joinedString)
    returnString = joinedString.split('_', maxTokens)[:-1]
    returnString = separator.join(returnString)
    print("returnStrirng:-", returnString)
    return returnString


def processOCR_result(res, origFileName='', threshold=0.1):
    # Processes OCR into a file name (full path)
    procName = []
    fileName = ''
    for (bbox, text, prob) in res:
        print(f"in for loop, text:{text}, prob:{prob} , orig:::{origFileName}")
        # break
        if prob > 0.1:
            print("Thresh above 0.1")
            print('---TEXT---', text)
            procName.append(text)

        else:
            print('No readable text')
        endName = list(ordered_set.OrderedSet(procName))
        fileName = conc_list(endName)
        print('procName: ', procName)
        full_text = ' '.join(procName)
        print("#### FULL TEXT OCR IS ===", full_text, "####")
        print(f"END LOOP ITEM _ fileName== {fileName}")
    return fileName

img = None
conced = None # placeholder for concatenated string
origNewDict = {}
destination = Path('C:\\', 'Users', 'Kris', 'Pictures', 'ocr_dest') # creating a valid path
destination = os.path.join(destination, '', '') #where the renamed memes go
for j in filepaths:
    print("ORIG", j)
    reader = easyocr.Reader(['en'], gpu=False)
    res = reader.readtext(j) # Res is a product of one read operation which can contain many items. It
    # is a Easyocr object
    final = hashlib.md5(j.encode('utf-8')).hexdigest()
    final = final+'.jpg'
    if res:
        orig_filename= ''
        for text in res:
            orig_filename = j
            print("TEXXXXXT:_", orig_filename, text)

        OCRres = processOCR_result(res, origFileName=j)
        final = f"{destination}{OCRres}.jpeg"
        if final == "C:/Users/Kris/memes/.jpeg": # If no text is OCRed
            os.rename(j, os.path.join(destination, final))
        print(f"##########orig::{j} -- Final filename:= {final}")
        # Img was successfully OCRed - now write to destination
        os.rename(j, os.path.join(destination, final)) # Writing to destination dir.
        origNewDict[j] = final
    # else:
    #     print(f"{j} has no readable text :(")
    #
    # break
    #     else:
    #         print('No readable text')
    #     conced = conc_list(newnames)
    # print('CONCED:::', conced)
    # print(f"src: -{j}- to be replaced with {conced}.jpg")
    # os.replace(j, conced)

print('THE dict:_::', origNewDict)
# ks = origNewDict.keys()
# for j in ks:
#
#     print(f'lklk : {origNewDict[j]} instaead of {j}')
#     os.rename(j, origNewDict[j])