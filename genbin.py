import sys

argv = sys.argv
argc = len(argv)

if argc < 2:
    print("利用方法:python genbin.py [inputfile] [outputfile]")
    quit()

file_binary = ''

count = 0

with open(argv[1], 'rb') as f:
    for c in f.read():
        crbin = bin(c)[2:]
        if len(crbin) < 8:
            crbin = ((8 - len(crbin)) * '0') + crbin
        print(crbin, end='')
        file_binary += crbin
        count += 1
        if count % 6 == 0:
            print()
        else:
            print(' ', end='')

print(count*8)

with open(argv[2], 'w') as f:
    f.writelines(file_binary)
