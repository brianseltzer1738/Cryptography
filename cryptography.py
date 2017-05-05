
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
b=list(associations)

x = 1
while x == 1: 
    wow = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if wow == "e":
        y = input("Message: ")
        g = input("Key: ")
        y = list(y)
        g = list(g)
        m = []
        for msg in y:
            m.append(associations.find(msg))
        n = []
        for msg in g:
            n.append(associations.find(msg))
        print(m,n)
        n=n*(len(y)//len(g)+1)
        print(n)
        mn=list(zip(m,n))
        print(list(mn))
        com=[]
        for a,b in mn: 
            com.append(a+b)
        print(com)
        fin=[]
        for y in com:
            fin.append(associations[y])
        print(fin)
        ans=''.join(fin)
        print(ans)
        if com>associations:
            
   
   
    if wow == "q":
        x = 2
    
 