def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))