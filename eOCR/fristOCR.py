import os
import hashlib
import easyocr
from os import listdir,rename
from PIL import Image
import ordered_set


myPath = r"C:\Users\Kris\Pictures\memes_OCR"
filepaths = [myPath+f for f in listdir(myPath)]
print(filepaths)
# We need to ID the img text.
# If text: Rename file with text .jpeg | rename with hash of orig ending in .jpeg


def splitter(n, string_, separator='_'):
    #Splits a string into a list of n pieces
    pieces = string_.split()
    return (separator.join(pieces[i:i+n]) for i in range(0, len(pieces), n))

def conc_list(the_list, separator='_', maxTokens=5):
# Joins list into string of max token size
#     sizedList = the_list[0:maxTokens+1]
    print("orig LIST ;;;", the_list)
    concedList = [i.replace(' ', '_') for i in the_list]
    print("Conced LIst===", concedList)
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

        else: #could search the filename for 4 or more consecutive chars and use these as filename.
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
destination = r"C:\Users\Kris\Pictures\OCR_landing"
for j in filepaths:
    print("ORIG", j)
    reader = easyocr.Reader(['en'], gpu=False)
    res = reader.readtext(j) # Res is a product of one read operation which can contain many items. It
    # is a Easyocr object

    if res:
        for text in res:
            print("TEXXXXXT:_", j, text)

        OCRres = processOCR_result(res, origFileName=j)
        final = f"{myPath}{OCRres}.jpeg"
        if final == "C:/Users/Kris/memes/.jpeg":
            final = hashlib.md5(j.encode('utf-8')).hexdigest()
            #See comment above
        print(f"##########orig::{j} -- Final filename:= {final}")
        # break
        origNewDict[j] = final
    else:
        print(f"{j} has no readable text :(")
        # os.rename(myPath, final)
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