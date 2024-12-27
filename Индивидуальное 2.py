import sys
import math
def find_min_abs_index(arr):
    if not arr:
        return None
    min_abs_val = abs(arr[0])
    min_abs_index = 0
    for i, val in enumerate(arr):
        if abs(val) < min_abs_val:
            min_abs_val = abs(val)
            min_abs_index = i
    return min_abs_index
def sum_abs_after_first_negative(arr):
    first_negative_index = next((i for i, val in enumerate(arr) if val < 0), None)
    if first_negative_index is None:
        return 0
    return sum(abs(val) for val in arr[first_negative_index + 1:])
def compress_list(arr, a, b):
    compressed_list = [x for x in arr if not (a <= x <= b)]
    compressed_list.extend([0] * (len(arr) - len(compressed_list)))
    return compressed_list
if __name__ == '__main__':
    try:
        input_str = input("Введите список вещественных чисел, разделенных пробелами: ")
        numbers = list(map(float, input_str.split()))
    except ValueError:
        print("Ошибка: Некорректный ввод. Пожалуйста, введите вещественные числа.", file=sys.stderr)
        sys.exit(1)

    if not numbers:
        print("Ошибка: Заданный список пуст.", file=sys.stderr)
        sys.exit(1)
    try:
        a = float(input("Введите левую границу интервала a: "))
        b = float(input("Введите правую границу интервала b: "))
    except ValueError:
      print("Ошибка: Некорректный ввод. Пожалуйста, введите вещественные числа для границ интервала.", file=sys.stderr)
      sys.exit(1)
    min_abs_index = find_min_abs_index(numbers)
    sum_after_negative = sum_abs_after_first_negative(numbers)
    compressed_numbers = compress_list(numbers, a, b)
    if min_abs_index is not None:
        print(f"Индекс элемента с минимальным модулем: {min_abs_index}")
    else:
      print("В списке нет элементов")
    print(f"Сумма модулей после первого отрицательного элемента: {sum_after_negative}")
    print(f"Сжатый список: {compressed_numbers}")