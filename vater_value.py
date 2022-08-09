def water_value(List_value):
    left = 0
    right = len(List_value) - 1
    Sum = 0
    while left < right:
        if List_value[left] > List_value[right]:
            temp = List_value[right] * (right - left)
            right -= 1

        else:
            temp = List_value[left] * (right - left)
            left += 1
        Sum = max(Sum, temp)
    return Sum


if __name__ == '__main__':
    print(water_value([1, 2, 4, 3, 5, 8, 1]))
