with open('D:\\Desktop\\out.txt', 'r') as input:
    with open('D:\\Desktop\\out0.txt', 'w') as output:
        for line in input:
            x = line.split('.')
            y = x[0]
            y = y[4:6]
            #print(y)
            output.write(y+' ')
    print("done")
			
