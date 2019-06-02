import itertools


def test_mas(a, n):
    ls_TF = [a[0]+a[1]+a[2] ==n,
             a[0] + a[1] + a[2] == n,
             a[3] + a[4] + a[5] == n,
             a[6] + a[7] + a[8] == n,
             a[0] + a[3] + a[6] == n,
             a[1] + a[4] + a[7] == n,
             a[2] + a[5] + a[8] == n,
             a[0] + a[4] + a[8] == n,
             a[6] + a[4] + a[2] == n,
             ]
    for i in ls_TF:
        if not i:
            break
    else:
        print(a[0],a[1],a[2])
        print(a[3] , a[4] , a[5])
        print(a[6] , a[7] , a[8])
        print('===================')

a = range(1, 10)
ls_comb = list(itertools.permutations(a, 9))
for i in ls_comb:
    test_mas(i, 15)