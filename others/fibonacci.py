def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 9
    for i in range(n):
       print(fibonacci(i), end=" ")