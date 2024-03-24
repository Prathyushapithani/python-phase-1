d={
    104:"a",
    103:"b",
    105:"d",
    106:"g",
    "104":"e"
}
d["104"]="o"
print(d)
d[165]="hello"
print(d)
for i in d:
    print(i)
for x in d.values():
    print(x)
for x,y in d.items():
    print(x,y)
d.pop(104)
print(d)
d[165]
print(d)