def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])
numbers = [5, 10, 15, 20]
result = recursive_sum(numbers)
print(f"Сумма элементов списка {numbers} равна {result}")