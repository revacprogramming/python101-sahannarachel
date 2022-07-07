# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
name = input("Enter file:")
fh=open(name)
sum=0
lst=list()
for line in fh:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    lst=lst+y
for i in lst:
    sum=sum+int(i)
print(sum)  