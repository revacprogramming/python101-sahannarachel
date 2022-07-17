# Using Web Services
# https://www.py4e.com/lessons/services
import urllib.request
import xml.etree.ElementTree as ET

result = 0

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()    
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print("Count:",len(counts))
for count in counts:
    value = count.text
    result = result + int(value)
print("Sum: ",result)
##Autograder 2
import urllib.request, json

address = input('Enter location: ')
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")
#print(data)
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)