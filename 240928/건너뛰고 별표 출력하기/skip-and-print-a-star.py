n = int(input())


for i in range(1, n+1):
    print('*' * i)
    print()

# n번째 줄 이후 별을 감소하는 순서로 출력
for i in range(n-1, 0, -1):
    print('*' * i)
    print()