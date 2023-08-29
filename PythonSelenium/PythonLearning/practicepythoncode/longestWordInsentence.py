import re
def longestWord(sentence):
    sen= re.split(" " ,sentence)
    print(sen,len(sen))
    c=max(sen,key=len) # max is used for get the max , key=len
    print(c,len(c))
    print(sorted(sen, key=len,reverse=True))
    res=sorted(sen, key=len,reverse=True) # sort based on len desc if reverse is true
    for x in res:
        print(x,len(x))



longestWord("the longest Word in sentence is char")

