#used to substitute the numbers found for part 2 to char
d_dict = {
        '01' : 'A','02' : 'B','03' : 'C','04' : 'D','05' : 'E','06' : 'F',
        '07' : 'G','08' : 'H','09' : 'I','10' : 'J','11' : 'K','12' : 'L',
        '13' : 'M','14' : 'N','15' : 'O','16' : 'P','17' : 'Q','18' : 'R',
        '19' : 'S','20' : 'T','21' : 'U','22' : 'V','23' : 'W','24' : 'X',
        '25' : 'Y','26' : 'Z','27' : '0','28' : '1','29' : '2','30' : '3',
        '31' : '4','32' : '5','33' : '6','34' : '7','35' : '8','36' : '9',
        '37' : 'a','38' : 'b','39' : 'c','40' : 'd','41' : 'e','42' : 'f',
        '43' : 'g','44' : 'h','45' : 'i','46' : 'j','47' : 'k','48' : 'l',
        '49' : 'm','50' : 'n','51' : 'o','52' : 'p','53' : 'q','54' : 'r',
        '55' : 's','56' : 't','57' : 'u','58' : 'v','59' : 'w','60' : 'x',
        '61' : 'y','62' : 'z','63' : '+','64' : '/',
}

with open('D:\\Desktop\\out0.txt', 'r') as input:
    with open('D:\\Desktop\\out1.txt', 'w') as output:
        for line in input:
            x = line.rstrip()
            #print(d_dict[x], end="")
            output.write(d_dict[x])
    print("done")

"""
with open('D:\\Desktop\\out.txt', 'r') as input:
    with open('D:\\Desktop\\out0.txt', 'w') as output:
        for line in input:
            x = line.split('.')
            y = x[0]
            y = y[4:6]
            #print(y)
            output.write(y+' ')
    print("done")
"""
