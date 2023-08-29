from collections import Counter

def countEle(sen):
    print(Counter(sen))
# to fetch only unique values
    c=Counter(sen)
    for x in c:
        print(x, c[x])
        if c[x]==1:
            print(x)

# another way
    print(list(k for k,v in c.items() if v==1))

countEle("wewrerea")

