import re
def removevowels(str1):
    sen= re.sub("a|e|i|o|u","",str1.lower())
    print(sen)
removevowels("aeiousdbyghk")
