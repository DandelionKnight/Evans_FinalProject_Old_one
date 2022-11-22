'''
Created on Nov 22, 2022

@author: myyna
'''
import json
englishFile = open('english.txt','r').readlines()

jsonFile = open('EncryptedGroupHints.json')

jsonDict = json.load(jsonFile)

hints = jsonDict['Evans']

print(hints)

print(type(englishFile))

print(englishFile[7479])

for x in hints:
    print(englishFile[int(x)])
   