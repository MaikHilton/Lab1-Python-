N = int(input("Введіть ціле число N (1 < N < 9): "))

if 1 < N < 9:
    # Верхня частина
    for i in range(N, 0, -1):
        print("5 " * i)
    # Нижня частина
    for i in range(2, N + 1):
        print("5 " * i)
else:
    print("Число N повинно бути в межах від 2 до 8.")
