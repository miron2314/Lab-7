if __name__ == '__main__':
    A = list(map(int, input("Введите 10 целых чисел через пробел: ").split()))
    if len(A) != 10:
        print("Ошибка: необходимо ввести ровно 10 целых чисел.", file=sys.stderr)
        exit(1)
    total_sum = sum(item for item in A if abs(item) < 5)
    print("Сумма элементов, меньших по модулю 5:", total_sum)
