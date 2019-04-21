'''i = []
k = " hi i am who r you"
wrd = k.split()
for s in wrd:
    i.append(s)
i.sort()
print(i)
c = []

for s in i:
    c.append(s)
c.sort()
print(c)
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst = []
for line in fh:
    h = line.split()
    for wrd in h:
        if wrd not in lst:
            lst.append(wrd)

lst.sort()
print(lst)
