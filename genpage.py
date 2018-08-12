import sys
import numpy
import math

argv = sys.argv
argc = len(argv)

if argc < 2:
    print("利用方法: python rebin.py [inputfile] [outputfile]")
    quit()

pix = 1024
binary = ''
with open(argv[1], 'rb') as inf:
    binary = inf.readline()
binary_str = binary.decode()

print((pix*pix)/2)
print(len(binary_str))
page_num = math.ceil(len(binary_str) / int((pix*pix)/2))
print(page_num)
