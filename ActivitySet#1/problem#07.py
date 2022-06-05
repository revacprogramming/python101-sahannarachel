# Strings

text = "X-DSPAM-Confidence:    0.8475"
string1=text.find("0")
data=text[string1: ]
print(float(data))  