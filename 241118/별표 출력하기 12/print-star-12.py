n= int(input())

for i in range(n):
    for j in range(n):
        if i == 0:  # 첫 번째 행
            print("* "* n)
        elif j == i and (j % 2 == 0 and i == 1):  # 조건에 맞는 열 출력
            print("* ", end=" ")
        else:
            print(" ", end=" ")
    print()  # 줄 바꿈
