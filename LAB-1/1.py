"""_summary_ : BASICS
"""
a, b = 10, 30
print(a+b, b-a)

a = "HEHEHE"
print(a[0:-2][::-1])

l = [10,20,30,40,50,60]
l = l[:-1][::-1]
l[1] = 400
for i, val in enumerate(l):
    if i != len(l)-1:
        print(val, end = ", ")
    else:
        print(val)

t = (10,20,30,40,50,60)
t = t[:-1][::-1]
try:
    t[1] = 400
except TypeError:
    pass
for i, val in enumerate(t):
    if i != len(t)-1:
        print(val, end = ", ")
    else:
        print(val)

d = {161: "Kunal", 184: "Rishi"}
d[185] = "Mihir"

print(d.keys())
print(d.values())
print(d)
