import sys
import math

def product_of_positives_multiples_of_3(arr):
    product = 1
    count = 0
    for num in arr:
        if num > 0 and num % 3 == 0:
            product *= num
            count += 1
    return product, count

if __name__ == '__main__':
    try:
        input_str = input("Введите список из 10 целых чисел, разделенных пробелами: ")
        numbers = list(map(int, input_str.split()))
    except ValueError:
        print("Ошибка: Некорректный ввод. Пожалуйста, введите целые числа.", file=sys.stderr)
        sys.exit(1)
    if len(numbers) != 10:
        print("Ошибка: Размер списка должен быть 10.", file=sys.stderr)
        sys.exit(1)
    product, count = product_of_positives_multiples_of_3(numbers)
    if count > 0:
        print(f"Произведение положительных элементов, кратных 3: {product}")
        print(f"Количество таких элементов: {count}")
    else:
        print("В списке нет положительных элементов, кратных 3.")