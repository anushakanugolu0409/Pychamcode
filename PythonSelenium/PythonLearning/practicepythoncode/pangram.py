import string
def pangram(sen):
    for x in sen:
        alphabets= string.ascii_lowercase
        if(set(sen.lower())>=set(alphabets)):
            return True

result= pangram("asafdkjjhfjqwertyuioplkjhgfdsazxcvbnm")
if (result== True):
    print("sen is pangr")
else:
    print("sen is not pangram")

