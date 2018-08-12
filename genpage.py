import sys
import numpy
import math

argv = sys.argv
argc = len(argv)

# if argc < 2:
#     print("利用方法: python rebin.py [inputfile] [outputfile]")
#     quit()

argv.append("./kouka.bin")

pix = 256
binary = ''
with open(argv[1], 'rb') as inf:
    binary = inf.readline()
binary_str = binary.decode()

max_bits = int((pix*pix)/2)
data_bits = len(binary_str)
page_num = math.ceil(len(binary_str) / max_bits)

over_bits = max_bits - data_bits
over_bytes = int(over_bits / 8)

print("ページサイズ:{0}x{0}".format(pix))
print("使用ページ数:" + str(page_num))
print("保存可能ビット:" + str(max_bits))
print("保存データビット:" + str(data_bits))
print("余剰ビット:" + str(over_bits))
print("余剰バイト:" + str(over_bytes))

for i in range(over_bytes):
    if i % 2 == 0:
        binary_str += "11101100"
    elif i % 2 == 1:
        binary_str += "00010001"

