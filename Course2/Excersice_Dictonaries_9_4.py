count_sender = dict()
max_sender = None
max_send = None

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith('From') and len(line.split()) == 7:
        sender = line.split()[1]
        count_sender[sender] = count_sender.get(sender, 0) + 1
        if max_send is None or count_sender[sender] > max_send:
            max_sender = sender
            max_send = count_sender[sender]

print(max_sender, max_send)
