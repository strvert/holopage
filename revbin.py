import sys
import struct

argv = sys.argv
argc = len(argv)

if argc < 2:
    print("利用方法: python rebin.py [inputfile] [outputfile]")
    quit()

binary = ''
with open(argv[1], 'rb') as inf:
    binary = inf.readline()
binary_str = binary.decode()

with open(argv[2], 'wb') as outf:
    for i in range(int(len(binary_str) / 8)):
        # print(hex(int(binary_str[:8], 2)) ,end="")
        outf.write(struct.pack("B", int(binary_str[:8], 2)))
        binary_str = binary_str[8:]
