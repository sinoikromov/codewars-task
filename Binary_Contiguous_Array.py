''' Task
На вход подается массив, состоящий из «0» и «1», также называемый двоичным массивом.

Задача

Найдите длину самого длинного непрерывного подмассива, состоящего из равного
количества «0» и «1».

Пример

s = [1,1,0,1,1,0,1,1]
         |_____|
            |
         [0,1,1,0]

         length = 4
Примечание

1<=длина(массив)<120000

[
( [0,1], 2),
( [0], 0),
( [1,1,0,1,1,0,1,1],4),
( [0,1,1,0,1,1,1,0,0,0],10),
( [0,0,1,1,1,0,0,0,0,0],6),
                                    ]:

'''


from itertools import accumulate

def binarray(s) -> int:
    arr = list(accumulate(1 if e else -1 for e in s))
    # longest contiguous sub array that adds to zero
    d = {}
    mx = 0
    for i, x in enumerate([0] + arr):
        if x in d:
            mx = max(mx, i - d[x])
        else:
            d[x] = i
    return mx



print(binarray([0, 1, 1, 0, 1, 1, 1, 0, 0, 0]))
