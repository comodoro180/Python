count_hours = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From') and len(line.split()) == 7:
        hour = line.split()[5]
        hour = hour.split(':')[0]
        count_hours[hour] = count_hours.get(hour, 0) + 1

hours_sorted = sorted([(k, v) for k, v in count_hours.items()])
for k, v in hours_sorted:
    print(k, v)
