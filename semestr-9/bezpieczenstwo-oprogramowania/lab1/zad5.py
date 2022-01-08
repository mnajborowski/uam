import sys

# f = open('file.txt')
f = open('/dev/urandom')
while 1:
    line = f.readline()
    if not line:
        break
    if sys.argv[1] in line:
        print(line)
