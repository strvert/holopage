import numpy as np
import cv2
import sys

argv = sys.argv
argc = len(argv)


if argc < 2:
    print("利用方法:python revpage.py [basename] [number_of_page] [outputfile]")
    quit()

page_num = int(argv[2])

page_list = []
for i in range(page_num):
    page_list.append(cv2.imread("{0}{1}.png".format(argv[1], i), cv2.IMREAD_GRAYSCALE) > 0)

pix = (page_list[0].shape)[0]
page_max_bits = int((pix ** 2) / 2)


print("ページサイズ:{0}x{0}".format(pix))
print("復号ページ数:{}".format(page_num))
print("復号開始")

read_binary_str = ""
count = 0
for page in range(page_num):
    page_point = page*page_max_bits
    for py in range(int(pix / 2)):
        for px in range(int(pix / 2)):
            # print(binary_str[count*2:(count*2)+2])
            if page_list[page][py*2][px*2+1] == True:
                read_binary_str += '00'
            elif page_list[page][py*2][px*2] == True:
                read_binary_str += '01'
            elif page_list[page][py*2+1][px*2+1] == True:
                read_binary_str += '10'
            elif page_list[page][py*2+1][px*2] == True:
                read_binary_str += '11'

            count += 1

if read_binary_str[-8:] == '11101100':
    code_type = 0
elif read_binary_str[-8:] == '00010001':
    code_type = 1
else:
    code_type = -1

out_binary_str = read_binary_str
for i in range(int(len(read_binary_str)/8)):
    if code_type == 0:
        out_binary_str = out_binary_str[:-8]
        if out_binary_str[-8:] == '00010001':
            code_type = 1
        else:
            code_type = -1
    elif code_type == 1:
        out_binary_str = out_binary_str[:-8]
        if out_binary_str[-8:] == '11101100':
            code_type = 0
        else:
            code_type = -1
    elif code_type == -1:
        if out_binary_str[-8:] == '00000000':
            out_binary_str = out_binary_str[:-8]
            print("復号完了")
            break
        else:
            print("Format error.")
            quit()

with open(argv[3], 'w') as f:
    f.writelines(out_binary_str)
