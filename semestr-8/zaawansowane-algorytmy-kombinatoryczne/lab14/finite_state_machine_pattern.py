# P = input()
P = 'aaba'
# T = input()
T = 'caabaabaabaabc'
alphabet = 'qwertyuiopasdfghjklzxcvbnm'

d = len(alphabet)
q = 0

n = len(T)
m = len(P)


def next_state(a):
    k = 0
    for _ in range(m + 1):
        if a in alphabet:
            k = min(m, q + 1)
            while not (P[1:q] + a).startswith(P[1:k]):
                k = k - 1
    return k


for i in range(n):
    q = next_state(T[i])
    if q == m:
        print(i - m)
