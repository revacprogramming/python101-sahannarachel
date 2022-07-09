# Dictionaries
name = input("Enter file:")
handle = open(name)
words=list()
counts=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From:'):        continue
    words=line.split()
    if words[1] not in counts:
        counts[words[1]]=1
    else:
        counts[words[1]]+=1
x=counts.values()
z=max(x)
for key in counts:
    if counts[key]==z:
        print(key,z)
