P = input()
T = input()

d = len('qwertyuiopasdfghjklzxcvbnm')
q = 47

n = len(T)
m = len(P)

h = pow(d, m - 1) % q
p = 0
t = 0

for i in range(m):
    p = (d * p + ord(P[i])) % q
    t = (d * t + ord(T[i])) % q

for s in range(n - m + 1):
    if p == t:
        if P[1:m] == T[s + 1:s + m]:
            print(s)
    if s < n - m:
        t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
