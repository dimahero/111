def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:
        return right

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def main():
    while True:
        try:
            sequence = input("Введите последовательность чисел через пробел: ")
            numbers = list(map(int, sequence.split()))
            break
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите последовательность целых чисел через пробел.")

    while True:
        try:
            user_number = int(input("Введите любое число: "))
            break
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число.")

    numbers = merge_sort(numbers)

    position = binary_search(numbers, user_number, 0, len(numbers) - 1)

    print("Отсортированный список:", numbers)
    if position >= len(numbers):
        print(
            "Нет элемента, который меньше введенного числа и за которым следует элемент, больший или равный введенному числу.")
    else:
        print("Позиция:", position)


main()