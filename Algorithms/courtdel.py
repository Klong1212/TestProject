
def alternatingCharacters(s):
    a=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            a+=1
    return a