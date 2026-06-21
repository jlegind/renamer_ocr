import uuid
from os import listdir,rename
from shutil import copyfile
import shutil


myPath = "C:/Users/Kris/Pictures/memes_OCR"
testPath = "C:/Users/Kris/Pictures/memes_res"
filepaths = [myPath+f for f in listdir(myPath)]
print('----',filepaths)

paths = filepaths[0:5]

print('PAAATHZ', paths)

def renamer(pathList):
    print('IN pathlist()()()', pathList)
    for j in pathList:
        spl = j.split("/")
        minus1string = spl[0:-1]
        print(minus1string)
        uid_name_ = '/'.join(minus1string)
        print('uid_name_ :', uid_name_)

        uid_name = uid_name_+"/"
        print('UID NAME!"#', uid_name)
        unid = uuid.uuid4()
        print(uid_name, unid, testPath+str(f"{unid}.jpeg"))
        write_path = testPath+str(f"{unid}.jpeg")
        with open(testPath, mode='w') as f:
            f.write(write_path)

        # copy(uid_name, testPath+str(f"{unid}.jpeg"))

renamer(paths)