rlist = 'abcdefggghijkkklmfaop'
x = []
y = []
lol = []
findict = []
count = 0
for i in rlist:
    x.append(i)

 

for z in x:
    l1 = '{}'.format(z), x.count('{}'.format(z))
    y.append(l1)

[lol.append(l1) for l1 in y if l1 not in lol]   

# print(lol[0][0])

for bap in lol:
    for tiste in bap:
        findict.append(tiste)
    
        # inv = (tiste[0] + tiste[1])
        # findict.append(inv)

print(findict)
        
# for y in x:
#     if y in x:
#         count += 1
#         print('{}: {}'.format(y,count))
#     if y not in x:
#         count = 1

    


#print(x)