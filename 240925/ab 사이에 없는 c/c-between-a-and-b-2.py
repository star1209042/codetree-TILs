a, b, c = map(int,input().split())

mul_c = False

for i in range(a, b+1):
    if i % c ==0:
        mul_c = True

if mul_c == False:
    print("YES")
else:
    print("NO")