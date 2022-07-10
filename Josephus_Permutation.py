'''

'''
def josephus(items, k):
    counter = 0
    dead = []
    while items:
        counter = (counter + k - 1) % len(items)
        dead.append(items.pop(counter))
    return dead


if __name__ == '__main__':
    print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))

'''
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
'''
