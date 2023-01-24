def c_t(a):
    tab=[]
    for i in range(0,26):
        tab.append(chr(i+a))
    return tab

Duze=c_t(65)
Male=c_t(97)

def isAlpha(a):
    if (ord(a)>=65 and ord(a)<65+26) or (ord(a)>=97 and ord(a)<97+26):
        return 1
    else:
        return 0
def isUpper(a):
    if (ord(a)>=65 and ord(a)<65+26):
        return 1
    else:
        return 0
def isLower(a):
    if (ord(a)>=97 and ord(a)<97+26):
        return 1
    else:
        return 0

def szyfr(string,D,M,tabkey_0,isAlpha,isUpper,isLower):
    zaszyfrowane=''
    tabkey=[]
    for k in range(0,len(tabkey_0)):
        diff=ord(tabkey_0[k])//len(D)
        tabkey.append(ord(tabkey_0[k])-diff*len(D))
        
    if len(tabkey)<len(string):
        diff=len(string)//len(tabkey)
    for h in range(0,diff):
        for f in range(0,len(tabkey)):
            tabkey.append(tabkey[f])
    p=0
    for i in range(0,len(string)):
        if isAlpha(string[i])==1:
            key=tabkey[p]
            if isUpper(string[i])==1:
                for j in range(0,len(D)):
                    if string[i]==D[j]:
                        if j+key<len(D):
                            zaszyfrowane+=D[j+key]
                        else:
                            zaszyfrowane+=D[j+key-len(D)]
            else:
                for j in range(0,len(M)):
                    if string[i]==M[j]:
                        if j+key<len(M):
                            zaszyfrowane+=M[j+key]
                        else:
                            zaszyfrowane+=M[j+key-len(M)]
            p=p+1
        else:
            zaszyfrowane+=string[i]
                    
    return zaszyfrowane
def main():
    print(szyfr("ALA?MA KOTA",Duze,Male,"PIES",isAlpha,isUpper,isLower))
    print(szyfr("W?ARSZAWA",Duze,Male,"LLLL",isAlpha,isUpper,isLower))
main()