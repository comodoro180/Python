fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
count = 0
fh = open(fname)
for line in fh:
    if line.startswith('From'):
        str = line.rstrip().split()
        if len(str) == 7:
            email = str[1]
            print(email)
            count = count + 1

print('There were', count, 'lines in the file with From as the first word')
