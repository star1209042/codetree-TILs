n = int(input())

for i in range(1, n):
    for k in range(i):
        print("*", end = " ")
    print()
for i in range(n):
    for j in range(n-i):
        print("*", end =" ")
    print()