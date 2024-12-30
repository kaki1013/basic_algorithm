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
# print(f"input..\na : {a_int}\nb : {b_int}\n")
# ab = 135 * 246
# N = 8
##############################

# define dft
def fft(arr):
    """ only for n=2^k """
    # f_k       = E_k + w_N^k * O_k
    # f_k+N//2  = E_k - w_N^k * O_k
    n = len(arr)
    if n == 1:
        return arr
    w_n = cos(-2 * pi / n) + sin(-2 * pi / n) * 1j
    w_nk = [w_n ** k for k in range(n)]  # w_Nk[k] = exp(-2ㅠi/N * k)

    even, odd = fft(arr[::2]), fft(arr[1::2])

    res = [0] * n
    for k in range(n//2):
        res[k] = even[k] + w_nk[k] * odd[k]
        res[k + n//2] = even[k] - w_nk[k] * odd[k]

    return res


# fft
a = fft(a)  # [a(w_N^0), a(w_N^1), ..]
b = fft(b)  # [b(w_N^0), b(w_N^1), ..]

# for debug
# print('after fft')
# print(a)
# print(b)
# print()

# polynomial multiplication : a and b
fft_ab = [a[i] * b[i] for i in range(N)]  # [(ab)(w_N^0), (ab)(w_N^1), ..]


# define inverse fft
def ifft(arr):
    arr = [a.conjugate() for a in arr]
    arr = fft(arr)
    arr = [a.conjugate()/N for a in arr]

    res = [round(a.real) for a in arr]
    return res  # [x0, x1, x2, ...]


# for debug
# print('after ifft')
# print(ifft(a))
# print(ifft(b))
# print()

# get coefficients of a*b
fft_ab = ifft(fft_ab)

# get value of a * b
ans = 0
for i in range(N):
    ans += fft_ab[i] * 10**i

# compare
if ans == ab:
    print(f'Success : {ab}')
else:
    print(f"Real Ans : {ab}")
    print(f"Your Ans : {ans}")
