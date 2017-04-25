
"""
cryptography.py
Author: Brian S.
Credit:
Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
To get a character's numeric representation, find the index of that character in the string 
(use the code associations.find(char) to get the index of char's first occurrence in associations)
To get a character back from this numeric representation, get the character at that number's index 
in the string (using associations[index]).
MUST ENCRYPT AND DECRYPT 
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
enumbers = []
ekeynumbers = []
enew = []
eend = []
dnumbers = []
dkeynumlist = []
dnewnums = []
dend = []
while command != "q":
    if command == "e":
        emessage = input("Message: ")
        ekey = input("Key: ")
        eeekey = ekey
        while len(ekey) < len(emessage):
            ekey = ekey + eeekey
        for x in emessage:
            enumbers.append(associations.find(x))
        for y in ekey:
            ekeynumbers.append(associations.find(y))
        ezip = list(zip(enumbers, ekeynumbers))
        for a in ezip:
            if a[0]+a[1] < len(associations):
                enew.append(a[0] + a[1])
            else:
                enew.append(a[0] + a[1] - len(associations))
        for i in enew:
            eend.append(associations[i])
        print(''.join(eend))
        enumbers = []
        ekeynumbers = []
        enew = []
        eend = []
    if command == "d":
        dmessage = input("Message: ")
        dkey = input("Key: ")
        deekey = dkey
        while len(dkey) < len(dmessage):
            dkey = dkey + deekey
        for x in dmessage:
            dnumbers.append(associations.find(x))
        for y in dkey:
            dkeynumlist.append(associations.find(y))
        dzip = list(zip(dnumbers, dkeynumlist))
        for a in dzip:
            if a[0]-a[1] >= 0:
                dnewnums.append(a[0] - a[1])
            else:
                dnewnums.append(a[0] - a[1] + len(associations))
        for i in dnewnums:
            dend.append(associations[i])
        print(''.join(dend))
        dnumbers = []
        dkeynumlist = []
        dnewnums = []
        dend = []
    if command != "d" and command != "e" and command !="q":
        print("Did not understand command, try again.")
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command == "q":
    print("Goodbye!")