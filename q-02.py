n=input()
S={ "d":1,"r":2,"m":3, "f":4,"s":5,"l":6,"c":7,}
T=[]
count=0
for i in range(len(n)):
    a=S.get(n[i])
    T.append(a)

T.insert(0,3)
print(T)

for o in range(len(n)):
    ab=(T[o]-T[o+1])
    if ab<0:
        ab=ab*-1
    count+=(ab+1)


print(count)