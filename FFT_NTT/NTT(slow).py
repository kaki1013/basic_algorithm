import random

# set parameter
DEBUG = True
MOD = 786433  # 2^18 * 3 + 1
ROOT = 10

MAX_LENGTH = 128
N = 1
while N <= 2 * MAX_LENGTH-1:
    N <<= 1

# generate input & answer
a_int = random.randint(1, 10 ** MAX_LENGTH-1)
b_int = random.randint(1, 10 ** MAX_LENGTH-1)
ab = a_int * b_int
print(f"input..\na : {a_int}\nb : {b_int}\n")

# pre-processing input data (idx = deg)
"""
ex. idx = deg
a : [a0 a1 a2 a3 0 0 0 0] : a0 + a1 x + a2 x^2 + a3 x^3 + ...
b : [b0 b1 b2 b3 0 0 0 0] : b0 + b1 x + b2 x^2 + b3 x^3 + ...
"""
a = list(map(int, str(a_int)))[::-1]
b = list(map(int, str(b_int)))[::-1]

a = a + [0] * (N - len(a))
b = b + [0] * (N - len(b))

##############################
if DEBUG:
    # test input data
    # a = [5, 3, 1, 0, 0, 0, 0, 0]  # 5 + 3x + x^2
    # b = [6, 4, 2, 0, 0, 0, 0, 0]  # 6 + 4x + 2x^2
    # print(f"input..\na : {a}\nb : {b}\n")
    # ab = 135 * 246
    # N = 8

    a = [3, 1, 0, 0]  # 3 + 1x
    b = [4, 2, 0, 0]  # 4 + 2x
    print(f"input..\na : {a}\nb : {b}\n")
    ab = 13 * 24
    N = 4
##############################
# pre-calculate w = "N-th" primitive root of unity (중요!)
w_N = pow(ROOT, (MOD - 1) // N, MOD)  # N-th primitive root


# define ntt
def ntt(arr):
    res = []
    for k in range(N):
        tmp = [(arr[n] * pow(w_N, n*k, MOD)) % MOD for n in range(N)]
        res.append(sum(tmp) % MOD)
    return res


# ntt
a = ntt(a)  # [a(w_N^0), a(w_N^1), ..]
b = ntt(b)  # [b(w_N^0), b(w_N^1), ..]

if DEBUG:
    # for debug
    print('after ntt')
    print(a)
    print(b)
    print()

# polynomial multiplication : a and b
ntt_ab = [(a[i] * b[i]) % MOD for i in range(N)]  # [(ab)(w_N^0), (ab)(w_N^1), ..]


# define inverse ntt
def intt(arr):
    # arr : [X0, X1, X2, ...]
    res = []
    for n in range(N):
        tmp = [(arr[k] * pow(w_N, -n*k, MOD)) % MOD for k in range(N)]
        res.append((sum(tmp) * pow(N, -1, MOD)) % MOD)
    return res  # [x0, x1, x2, ...]


if DEBUG:
    # for debug
    print('after intt')
    print(intt(a))
    print(intt(b))
    print()

# get coefficients of a*b
dft_ab = intt(ntt_ab)

# get value of a * b
ans = 0
for i in range(N):
    ans += dft_ab[i] * 10 ** i

# compare
if ans == ab:
    print(f'Success : {ab}')
else:
    print(f"Real Ans : {ab}")
    print(f"Your Ans : {ans}")
