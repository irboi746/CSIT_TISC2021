# written in python3, used to generate characters for dictionary file
x = 97
y = 37
while x < 128:
    print("'" + str(y)  +"' : '" + chr(x) + "'," )
    y+=1
    x+=1
    

