""""
На шахматной доске N x N находится M ладей(ладья бьёт клетки на той
же горизонт или вертикали до ближайщей занятой)
Определите сколко пар ладья бьёт друг друга

1 <= N <= 10 ** 9, 0 <= N <= 2 * 10 ** 5
"""


def countbeatngrooks(rookcoords):
    def addrook(rowolcol, key):
        if key not in rowolcol:
            rowolcol[key] = 0
        rowolcol[key] += 1

    def countpainrs(rowolcol):
        pairs = 0
        for key in rowolcol:
            pairs += rowolcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rookcoords, row)
        addrook(rooksincol, col)
    return countpainrs(rooksinrow) + countpainrs(rooksincol)