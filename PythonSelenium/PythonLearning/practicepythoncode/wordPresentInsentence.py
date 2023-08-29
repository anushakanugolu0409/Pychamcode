import re

def wordinSen(sent, word):
    sen = re.split("\s",sent)
    print(sen)
    for x in sen:
        if(x==word):
            return True

sen=input("Enter the sentence")
word=input("Enter the word")

result = wordinSen(sen,word)
if result == True:
    print("word is present")
else:
    print("not present")

