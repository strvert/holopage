import sys
import numpy as np
import math
from PIL import Image

np.set_printoptions(edgeitems=10)

argv = sys.argv
argc = len(argv)

if argc == 4:
    pix = int(argv[3])
else:
    pix = 1024

binary = ''
with open(argv[1], 'rb') as inf:
    binary = inf.readline()
binary_str = str(binary.decode()) + "00000000"

page_max_bits = int((pix*pix)/2)
data_bits = len(binary_str)
data_bytes = int(data_bits / 8)
page_num = math.ceil(len(binary_str) / page_max_bits)
total_max_bits = page_num * page_max_bits

over_bits = total_max_bits - data_bits
over_bytes = int(over_bits / 8)

print("ページサイズ:{0}x{0}".format(pix))
print("使用ページ数:{}".format(page_num))
print("ページ保存可能ビット:{}".format(page_max_bits))
print("合計保存可能ビット:{}".format(total_max_bits))
print("保存データビット:{}".format(data_bits))
print("保存データバイト:{}".format(data_bytes))
print("余剰ビット:{}".format(over_bits))
print("余剰バイト:{}".format(over_bytes))
print()
print("生成開始")

for i in range(over_bytes):
    if i % 2 == 0:
        binary_str += "11101100"
    elif i % 2 == 1:
        binary_str += "00010001"

page_arrays = np.zeros((page_num, pix, pix))

#print(binary_str[:100])

count = 0
for page in range(page_num):
    page_point = page*page_max_bits
    page_binary = binary_str[page_point:]
    for py in range(int(pix / 2)):
        for px in range(int(pix / 2)):
            pix_point = px
            # print(binary_str[count*2:(count*2)+2])
            if binary_str[count*2:(count*2)+2] == '00':
                page_arrays[page][py*2][px*2+1] = 255
            elif binary_str[count*2:(count*2)+2] == '01':
                page_arrays[page][py*2][px*2] = 255
            elif binary_str[count*2:(count*2)+2] == '10':
                page_arrays[page][py*2+1][px*2+1] = 255
            elif binary_str[count*2:(count*2)+2] == '11':
                page_arrays[page][py*2+1][px*2] = 255
            count += 1

for page in range(page_num):
    Image.fromarray(page_arrays[page]).convert("L").save("{0}{1}.png".format(argv[2], page))

