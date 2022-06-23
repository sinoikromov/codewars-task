def victor_good(worth, good):
    List_worth = list(map(int, good.split()))
    for i in range(len(List_worth)):
        List_worth[i] *= worth[i]
    return sum(List_worth)


def good_vs_evil(good, evil):
    worth_good = [1, 2, 3, 3, 4, 10]
    worth_evil = [1, 2, 2, 2, 3, 5, 10]
    good = victor_good(worth_good, good)
    evil = victor_good(worth_evil, evil)
    if good > evil:
        return "Battle Result: Good triumphs over Evil"
    elif evil > good:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return 'Battle Result: No victor on this battle field'


if __name__ == '__main__':
    good = '1 0 0 0 0 0'
    evil = '1 0 0 0 0 0 0'
    print(good_vs_evil(good, evil))
ss