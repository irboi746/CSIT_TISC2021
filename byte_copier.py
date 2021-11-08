def copy_byte(endoffset, x):
        a = 148
        start_offset = endoffset-147
        out = ""
        while (a > 0):
                out += hex(x[start_offset]).replace("0x","").ljust(2, "0")+' '
                #out = print(hex(x[start_offset]).replace("0x","").ljust(2, "0"), end=" ")
                start_offset += 1
                a -=1
       # print('\n')
        return out
        
with open('C:\\Users\\aaa\\Desktop\\Stage3\\1_edited.bmp','rb') as input:
        with open('C:\\Users\\aaa\\Desktop\\Stage3\\no1.txt', 'w') as output:
                x = input.read()
                aggregated = ""
                offset = len(x)-1
                while (offset > 0):
                        #copy_byte(offset, x)
                        aggregated += copy_byte(offset, x) + ' '
                        offset -= 148
                output.write(aggregated)
                
                
