import ordered_set as ose
import os
import hashlib
import Levenshtein

ll = [1,2,3,4,4,5,6,7]

nl = list(ose.OrderedSet(ll))

print(nl)

pieces = ['Blacks_without_whites', 'Whites_without_Blacks', 'ILede_with_mematic']
pieces = '_'.join(pieces)
print('join pieces:_', pieces)
piec = pieces.split('_', 5)[:-1]
print('pieC', piec)
conced = '_'.join(piec)
print('conced:', conced)
def splitter(n, string_, separator='_'):
    #splites a string n times
    pieces = string_.split()
    print('Peiecesss', pieces)
    return ('_'.join(pieces[i:i+n]) for i in range(0, len(pieces), n))

res = splitter(2, conced)
# print(list(res))
for j in res:
    print(j)
    break

orgFile = r"C:\Users\Kris\PycharmProjects\eOCR\shit.txt"
newName = r"C:\Users\Kris\PycharmProjects\eOCR\piss.txt"

# os.rename(orgFile, newName)

final = "C:/Users/Kris/memes/AlexJonesLOL.jpg"
final2 = hashlib.md5(j.encode('utf-8')).hexdigest()
print('hashed md5---', final2)


s1 = "Kris"
s2 = "krist "

rr = Levenshtein.distance(s1,s2)
print(f"Leven dist = {rr}")