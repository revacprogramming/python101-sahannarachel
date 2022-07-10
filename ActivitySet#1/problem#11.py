# Tuples
filename = "dataset/mbox-short.txt"

name = input("Enter file:")
handle = open(name)
counts=dict()
lst=list()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):        continue
    words = line.split()
    x=words[5]
    y=x[ :2]
    lst.append(y)
lst.sort()
for x in lst:
    counts[x]=counts.get(x,0)+1
sorted(counts.items())
for key, val in sorted(counts.items()):
    print(key,val)