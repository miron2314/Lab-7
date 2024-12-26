def count_positive_between_min_max(lst):
    if not lst:
        return 0
    min_value = min(lst)
    max_value = max(lst)
    min_index = lst.index(min_value)
    max_index = lst.index(max_value)
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)
    positive_count = sum(1 for x in lst[start_index:end_index] if x > 0)
    return positive_count
if __name__ == '__main__':
    A = list(map(int, input("Введите целые числа через пробел: ").split()))
    result = count_positive_between_min_max(A)
    print("Количество положительных элементов между максимальным и минимальным:", result)
