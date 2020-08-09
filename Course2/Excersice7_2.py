# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
number_lines = 0
acum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    # print(line)
    number_lines = number_lines + 1
    acum = acum + float(line[line.find(':')+1:].strip())

if number_lines > 0:
    avgr = acum/number_lines
    print('Average spam confidence:', avgr)

