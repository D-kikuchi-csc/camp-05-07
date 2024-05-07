n=int(input())
l= list(map(int, input().split()))
myset=set()
for i in range(n):
    myset.add(l[i])
if n==len(myset):
    print("YES")
else:
    print("NO")