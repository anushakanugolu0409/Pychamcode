from collections import Counter
import re
def uniqueChar(sen1):
    sen=re.split("\s",sen1)
    res=Counter(sen)
    print(res, len(res), len(sen))
    if (len(sen)==len(res)):
        print("str is unique char")
    else:
        print('no unique char')
uniqueChar("sagb wqe fddd oiu fddd")
