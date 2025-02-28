
def alternatingCharacters(s):
    a=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            a+=1
            
    return a
if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)
