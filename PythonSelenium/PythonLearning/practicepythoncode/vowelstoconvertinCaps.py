def vowelcon(strings):
    a=[]
    for x in strings:
        if x in ("a|e|i|o|u"):
            t=x.upper()
            a.append(t)
        else:
            t=x.lower()
            a.append(t)
    return "".join(a)#conversion of list to str

results=vowelcon(input("enter the string"))
print(results)
