import re


pattern = re.compile("this")
string = "search this inside of this text please"

a = pattern.search(string)
b = pattern.findall(string)

print(a.span())
print(a.start())
print(a.end())
print(a.group())
print(b)
