# 11500 참고
"""
goal : given k, determine a_i for 0 <= i <= k+1
    where sum_{i=1}^{n} i^k = 1^k + 2^k + ... + n^k = a_{k+1}*n^{k+1} + a_{k}*n^{k} + ... + a_1*n + a_0
    ex) k = 0: 0 + 1n
        k = 1: 0 + n/2 + n^2/2
        k = 2: 0 + n/6 + n^2/2 + n^3/3
        k = 3: 0 + 0n + n^2/4 + n^3/2 + n^4/4

1. sum_{i=1}^{n} i^k 의 점화식 계산
(n+1)^(k+1) - n^(k+1)       = C(k+1, 1)*n^k     + C(k+1, 2)*n^(k-1)     + ... + C(k+1, t)*n^(k-t+1)     + ... + 1
를 이용하자. 단, C는 combination(nCr = C(n,r))을 의미함

2^(k+1)     - 1^(k+1)       = C(k+1, 1)*1^k     + C(k+1, 2)*1^(k-1)     + ... + C(k+1, t)*1^(k-t+1)     + ... + 1
...
n^(k+1)     - (n-1)^(k+1)   = C(k+1, 1)*(n-1)^k + C(k+1, 2)*(n-1)^(k-1) + ... + C(k+1, t)*(n-1)^(k-t+1) + ... + 1
(n+1)^(k+1) - n^(k+1)       = C(k+1, 1)*n^k     + C(k+1, 2)*n^(k-1)     + ... + C(k+1, t)*n^(k-t+1)     + ... + 1
의 양변을 모두 더한 뒤에 식을 정리하면,

(n+1)^(k+1) - 1^(k+1)       = C(k+1, 1)*[sum_{i=1}^{n} i^k] + C(k+1, 2)*[sum_{i=1}^{n} i^{k-1}] + ... + C(k+1, t)*[sum_{i=1}^{n} i^{k-t+1}] + ... + 1 * n
이므로, C(k+1, 1)*[sum_{i=1}^{n} i^k] = (k+1)*[sum_{i=1}^{n} i^k] 항만을 좌변에 남기면
(k+1)*[sum_{i=1}^{n} i^k]   = (n+1)^(k+1) - 1
                                - C(k+1, 2)*[sum_{i=1}^{n} i^{k-1}] - ... - C(k+1, t)*[sum_{i=1}^{n} i^{k-t+1}] - ... - C(k+1, k)*[sum_{i=1}^{n} i^{1}]
                                    - n
이 된다.

즉, 식을 정리하면
(k+1)*[sum_{i=1}^{n} i^k]   = (n+1)^(k+1) - 1 - n
                                - C(k+1, 2)*[sum_{i=1}^{n} i^{k-1}] - ... - C(k+1, t)*[sum_{i=1}^{n} i^{k-t+1}] - ... - C(k+1, k)*[sum_{i=1}^{n} i^{1}]

2. dp 구성
위의 문제 상황을 해결하기 위해, 다음과 같은 dp table을 생각하자.

(1) dp 정의
0 <= degree <= k, 0 <= term <= degree+1 <= k+1 인 degree, term에 대해서
dp[degree][term] := [sum_{i=1}^{n} i^degree](=n에 대한 (degree+1)차식) 에서 n^term의 계수..에 (k+1)!을 곱한 값
    ((k+1)!을 곱하는 것은 정수형으로 만들어주기 위함, 마지막에 나누어주면 분수꼴로 나타낼 수 있음)

(2) 관계식
dp[degree] = [(n+1)^(degree+1) - 1 - n - C(degree+1, 2)*dp[degree-1] - ... - C(degree+1, t)*dp[degree-t+1] - ... - C(degree+1, degree)*dp[1]] // (degree+1)

(3) 답
given k, a_i = dp[k][i] // (k+1)!
    for 0 <= i <= k+1
        where sum_{i=1}^{n} i^k = 1^k + 2^k + ... + n^k = a_{k+1}*n^{k+1} + a_{k}*n^{k} + ... + a_1*n + a_0
"""
from math import factorial
from math import gcd


def binomial_coefficient(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))


k = int(input())
k1_factorial = factorial(k+1)
dp = [[0 for _ in range((k+1)+1)] for _ in range(k+1)]  # k이하 == (k+1)미만 : dp[k] 접근하기 위함

# dp[0] initialization
dp[0][1] = k1_factorial  # dp[0] := [(0 + 1*n)*k1_factorial] 의 계수

"""
dp[degree] = [(n+1)^(degree+1) - 1 - n - C(degree+1, 2)*dp[degree-1] - ... - C(degree+1, t)*dp[degree-t+1] - ... - C(degree+1, degree)*dp[1]] // (degree+1)
(1) dp[degree] = (n+1)^(degree+1)
(2) dp[degree][0] -= 1; dp[degree][1] -= 1;
(3) 이전 dp는 k1_factorial을 곱해서 관리되고 있으므로, 현재 [(n+1)^(degree+1) - 1 - n]까지 k1_factorial을 곱함
(4) - C(degree+1, 2)*dp[degree-1] - ... - C(degree+1, t)*dp[degree-t+1] - ... - C(degree+1, degree)*dp[1] 를 수행
(5) (degree+1) 을 나눔
"""
for degree in range(1, k+1):
    # (1) dp[degree] = (n+1)^(degree+1)
    for term in range((degree+1)+1):
        dp[degree][term] += binomial_coefficient(degree+1, term)
    # (2) dp[degree][0] -= 1; dp[degree][1] -= 1;
    dp[degree][0] -= 1
    dp[degree][1] -= 1
    # (3) 이전 dp는 k1_factorial을 곱해서 관리되고 있으므로, 현재까지 구한 [(n+1)^(degree+1) - 1 - n]에 k1_factorial을 곱함
    for term in range((degree+1)+1):
        dp[degree][term] *= k1_factorial
    # (4) - C(degree+1, 2)*dp[degree-1] - ... - C(degree+1, t)*dp[degree-t+1] - ... - C(degree+1, degree)*dp[1] 를 수행
    for prev_degree in range(1, degree):
        for term in range((prev_degree+1)+1):
            dp[degree][term] -= binomial_coefficient(degree+1, prev_degree) * dp[prev_degree][term]
    # (5) (degree+1) 을 나눔
    for term in range((degree+1)+1):
        dp[degree][term] //= (degree+1)


"""
testcase : 10
n^10의 합은 '5x/66 - x^3/2 + x^5 - x^7 + 5x^9/6 + x^10/2 + x^11/11'
    -> (5*n - 33*n**3 + 66*n**5 - 66*n**7 + 55*n**9 + 33*n**10 + 6*n**11)//66
"""
def print_coef():
    # 분수꼴로 확인하려면 'dp[i][j] / nftr' 을 약분하면 끝
    for term in range(k+2):
        up = dp[k][term]
        down = k1_factorial

        GCD = gcd(abs(up), down)
        up //= GCD
        down //= GCD

        coef = f'{up} / {down}' if up % down else f'{up//down}'
        print(f"x^{term}의 계수는 {coef}")


print_coef()
