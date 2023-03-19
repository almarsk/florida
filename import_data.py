import requests
import json

links = {"A-B": "http://w3.usf.edu/FreeAssociation/AppendixB/A-B.TargetsCues",
         "C":   "http://w3.usf.edu/FreeAssociation/AppendixB/C.TargetsCues",
         "D-F": "http://w3.usf.edu/FreeAssociation/AppendixB/D-F.TargetsCues",
         "G-K": "http://w3.usf.edu/FreeAssociation/AppendixB/G-K.TargetsCues",
         "L-O": "http://w3.usf.edu/FreeAssociation/AppendixB/L-O.TargetsCues",
         "P-R": "http://w3.usf.edu/FreeAssociation/AppendixB/P-R.TargetsCues",
         "S":   "http://w3.usf.edu/FreeAssociation/AppendixB/S.TargetsCues",
         "T-Z": "http://w3.usf.edu/FreeAssociation/AppendixB/T-Z.TargetsCues"}

data = dict()

for index, link in links.items():
    data[index] = requests.get(link)

for chunk in data:
    json_string = json.dumps(data[chunk].text)

    with open('florida.txt', 'a+') as f:
        f.write(json_string)
