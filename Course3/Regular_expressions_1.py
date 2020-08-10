import re

all_numbers = list()
total = 0
fh = open('regex_sum_825113.txt')
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        all_numbers = all_numbers + numbers

for number in all_numbers:
    total = total + int(number)

print(total)
