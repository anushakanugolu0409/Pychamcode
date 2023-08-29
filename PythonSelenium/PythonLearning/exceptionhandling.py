
try:
    x= int(input("enter the value for x"))
    y= int(input("enter the value for y"))
    if y==0:
        raise Exception ("y value should be grater than 0")
    print(x/y)

except Exception as e:
    print(e)
    print("enter valid values, as there is exception with denominator 0")

else:
    print("enter values are correct")

finally:
    print("in all cases finally is exceuted")
