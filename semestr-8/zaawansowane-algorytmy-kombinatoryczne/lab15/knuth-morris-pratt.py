P = input()
T = input()

q = 0

m = len(P)
n = len(T)


def get_pi():
    pi = [0] * m
    pi[0] = 0
    k = 0
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k - 1]
        if P[k] == P[i]:
            k = k + 1
        pi[i] = k
    return pi


pi = get_pi()
for i in range(n):
    while q > 0 and P[q] != T[i]:
        q = pi[q - 1]
    if P[q] == T[i]:
        q = q + 1
    if q == m:
        print(i - m + 1)
        q = pi[q - 1]
