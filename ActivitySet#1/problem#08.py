# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
s=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    string1=line.find("0")
    data=float(line[string1: ])
    s=s+data
    count=count+1
average=s/count
print("Average spam confidence:",average)
