import random
from math import sin, cos, pi

# set parameter
MAX_LENGTH = 1024
N = 1
while N <= 2*MAX_LENGTH:
    N <<= 1

# generate input & answer
a_int = random.randint(1, 10 ** MAX_LENGTH)
b_int = random.randint(1, 10 ** MAX_LENGTH)
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
# test input data
# a = [5, 3, 1, 0, 0, 0, 0, 0]  # 5 + 3x + x^2
# b = [6, 4, 2, 0, 0, 0, 0, 0]  # 6 + 4x + 2x^2
# print(f"input..\na : {a}\nb : {b}\n")
# ab = 135 * 246
# N = 8
##############################

# pre-calculate 'root of unity'
w_N = cos(-2 * pi / N) + sin(-2 * pi / N) * 1j
w_Nk = [w_N ** k for k in range(N)]  # w_Nk[k] = exp(-2ㅠi/N * k)


# define dft
def dft(arr):
    res = []
    for k in range(N):
        tmp = [arr[n] * w_Nk[(k * n) % N] for n in range(N)]
        res.append(sum(tmp))
    return res


# dft
a = dft(a)  # [a(w_N^0), a(w_N^1), ..]
b = dft(b)  # [b(w_N^0), b(w_N^1), ..]

# for debug
# print('after dft')
# print(a)
# print(b)
# print()

# polynomial multiplication : a and b
dft_ab = [a[i] * b[i] for i in range(N)]  # [(ab)(w_N^0), (ab)(w_N^1), ..]


# define inverse dft
def idft(arr):
    # arr : [X0, X1, X2, ...]
    res = []
    for n in range(N):
        # w_Nk[k] = exp(-2ㅠi/N * k) 임을 이용
        tmp = [arr[k] * w_Nk[(k * n) % N].conjugate() for k in range(N)]
        res.append(sum(tmp).real / N)

    res = [round(res[n]) for n in range(N)]
    return res  # [x0, x1, x2, ...]

# for debug
# print('after idft')
# print(idft(a))
# print(idft(b))
# print()

# get coefficients of a*b
dft_ab = idft(dft_ab)

# get value of a * b
ans = 0
for i in range(N):
    ans += dft_ab[i] * 10**i

# compare
if ans == ab:
    print(f'Success : {ab}')
else:
    print(f"Real Ans : {ab}")
    print(f"Your Ans : {ans}")
