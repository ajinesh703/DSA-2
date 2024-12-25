def binary_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(i % 2) for _ in range(1, i + 1)))

n = int(input("Enter the number of rows: "))
binary_triangle(n)
