n = int(input())

for i in range(n):
    print("  "*(i), end = "")
    print("*", end = " ")
    for j in range(n-i-1):
        print("* "*2, end = "")
    print()

for i in range(n-1):
    print("  "*(n-i-2), end = "")
    print("*", end = " ")
    for k in range(i+1):
        print("* "*2, end = "")
    print()