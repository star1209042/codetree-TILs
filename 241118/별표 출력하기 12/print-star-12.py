n = int(input())

for i in range(n):
    if i == 0:  # 첫 줄
        print("* " * n)
    elif i % 2 == 1:  # 홀수 번째 줄
        for j in range(n):
            if j == i // 2 or j == n - i // 2 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    else:  # 짝수 번째 줄 (빈 공간 줄)
        for j in range(n):
            if j == n - i // 2 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
