l=[1,2,3,4,5]
with open("C:\\learnpythonfilereannwrite\\text.txt","w") as f:

    for x in l:
        f.write(str(x)+ "\n") # to write to file it shd be in str so type caste as str

with open("C:\\learnpythonfilereannwrite\\text.txt","a") as f:
     f.write("\n"+ "write the next line of code")

with open ("C:\\learnpythonfilereannwrite\\text.txt","r") as f:
    print(f.read())
f.close()
