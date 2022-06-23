'''  ОПИСАНИЕ:
Вам будет дан массив чисел. Вы должны отсортировать нечетные числа в
порядке возрастания, оставив четные числа на их исходных позициях.

Примеры:

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

'''


def sort_array(source_array):
    for i in range(len(source_array) - 1):
        if source_array[i] % 2 != 0:
            for j in range(i + 1, len(source_array)):
                if source_array[i] > source_array[j] and source_array[j] % 2 != 0:
                    source_array[i], source_array[j] = source_array[j], source_array[i]
    return source_array


if __name__ == '__main__':
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(sort_array(array))
