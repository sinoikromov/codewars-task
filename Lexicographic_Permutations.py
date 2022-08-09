import itertools


def nth_perm(n, d):
    s = list((range(0, d)))
    k = itertools.permutations(s, len(s))
    for i, j in enumerate(k):
        if i+1 == n:
            return ''.join(map(str, j))



if __name__ == '__main__':
    print(nth_perm(1,1))
