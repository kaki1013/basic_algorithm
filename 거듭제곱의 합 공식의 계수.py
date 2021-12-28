# BOJ 11500
"""
sigma (k=1 ~ k=n) k^i = 1^i + 2^i + ... + n^i
ex)
i = 0: 0 + 1n
i = 1: 0 + n/2 + n^2/2
i = 2: 0 + n/6 + n^2/2 + n^3/3
i = 3: 0 + 0n + n^2/4 + n^3/2 + n^4/4

다음과 같은 dp table 을 생각하자.
0 <= i <= n, 0 <= j <= n+1 인 i, j에 대해서
dp[i][j] := n+1차식인 sigma(1<=k<=n) k^i 에서 n^j의 계수 * (n+1)!
i = 식의 order, j = 항의 order
((n+1)!을 곱하는 것은 정수형으로 만들어주기 위함, 마지막에 나누어주면 분수꼴로 나타낼 수 있음)
"""
from math import factorial as ftr
from math import gcd


def binomial_coefficient(n, k):
    return ftr(n)//(ftr(n-k)*ftr(k))


n = 25 + 1  # 25이하 == 26미만
nftr = ftr(n)  # 26!
dp = [[0 for _ in range(n+1)] for _ in range(n)]
dp[0][1], dp[1][1], dp[1][2] = nftr, nftr//2, nftr//2

for i in range(2, n):

    for j in range((i+1)+1):
        dp[i][j] += binomial_coefficient(i+1, j)

    dp[i][0] -= 1
    dp[i][1] -= 1

    for j in range((i+1)+1):
        dp[i][j] *= nftr

    for order in range(1, i):
        for term in range((order+1)+1):
            dp[i][term] -= binomial_coefficient(i+1, order) * dp[order][term]  # dp[order][term]은 nftr이 곱해진 상태

    for j in range((i+1)+1):
        dp[i][j] //= (i+1)


# ex: sigma x^4 계수 확인 -> 분수꼴로 확인하려면 'dp[i][j] / nftr' 을 약분하면 끝
# ex: n^10의 합은 '5x/66 - x^3/2 + x^5 - x^7 + 5x^9/6 + x^10/2 + x^11/11'
# (5*n - 33*n**3 + 66*n**5 - 66*n**7 + 55*n**9 + 33*n**10 + 6*n**11)//66
check = int(input('확인하고 싶은 차수(0~25)를 숫자만 입력해주세요 : '))
for i in range(check, check+1):
    for j in range(i+2):
        up = dp[i][j]
        down = nftr
        GCD = gcd(abs(up), down)
        up //= GCD
        down //= GCD
        print(f'x^{j}의 계수는 {up} / {down}' if up % down else f'x^{j}의 계수는 {up//down}')

#for n in dp[4][:6]:
#    print(n/nftr)