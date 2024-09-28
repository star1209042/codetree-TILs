n = int(input())

for i in range(n):
    print("* "* (2*n-2*i-1))
    print("  "*(i), end = "  ")
print()