def number_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))

n = int(input("Enter the number of rows: "))
number_pyramid(n)
