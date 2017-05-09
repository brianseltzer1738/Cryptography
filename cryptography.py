
"""
cryptography.py
Author: Brian S.
Credit: Finn and Mr. D
Assignment:
+KF;B(CH=NIZ}m;R\Dt
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
        n=n*(len(y)//len(g)+1)
        mn=list(zip(m,n))
        com=[]
        for a,b in mn: 
            r=a+b
            if r>len(associations):
                r-=len(associations)
            com.append(r)
        fin=[]
        for y in com:
            fin.append(associations[y])
        ans=''.join(fin)
        print(ans)
        
    elif wow == "d":
        yd = input("Message: ")
        gd = input("Key: ")
        yd = list(yd)
        gd = list(gd)
        md = []
        for msg in yd:
            md.append(associations.find(msg))
        nd = []
        for msg in gd:
            nd.append(associations.find(msg))
        nd=nd*(len(yd)//len(gd)+1)
        mdnd=list(zip(md,nd))
        comd=[]
        for ad,bd in mdnd: 
            rd=ad-bd
            if rd>len(associations):
                rd-=len(associations)
            comd.append(rd)
        find=[]
        for yd in comd:
            find.append(associations[yd])
        ansd=''.join(find)
        print(ansd) 
    elif wow == "q":
        print("Goodbye")
        print("")
        x = 2
    else:
        print("Did not understand command, try again.")
        

 