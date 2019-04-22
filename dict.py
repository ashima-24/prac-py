name = input("Enter file:")
di = dict()
c = 0
handle = open(name)
for line in handle:
    if line.startswith('From'):
        #print(line)
        l = line.split()
        if l[0] == 'From':
            #print(l[1])
            x =	l[1]
            if x not in di:
            	di[x] = 1
            else:
                di[x] = di.get(x,0) +1
for key,val in di.items():
    if val > c:
        c = val
        r = key


print(r,c)


