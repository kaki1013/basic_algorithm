def gcd(a, b):
    if b == 0:
        return 1,0,a
    x, y, g = gcd(b, a%b)
    return y, x-(a//b)*y, g

"""
ax+by=g 를 만족하는 x, y?	(g = gcd(a, b))

아래 식을 만족하는 x', y'을 안다고 가정
bx' + (a%b)y' = g

그러면 a%b = a - (a//b) * b 이므로
bx' + (a%b)y' = g 에서
bx' + (a - (a//b) * b)y' = g

식을 정리하면
ay' + b(x' - (a//b) * y') = g
이므로, 원래 문제에서 x=y', y=x' - (a//b) * y'

이때 기저조건은
처음 식에서 a=g, x=1, y=0, g=a
"""


p = 26513
q = 32321
# p * u + q * v = gcd(p,q)
print(gcd(p, q))
