# Dictionaries
name = input("Enter file:")
fh=open(name)
words=list()
counts =dict()
for line in fh:
    if line.startswith("From:"):
        words=line.split()
        if words[1] not in counts:
            counts[words[1]]=1
        else:
            counts[words[1]]+=1
you=counts.values()
z=max(you)
for key in counts:
    if counts[key]==z:
        print(key,z)