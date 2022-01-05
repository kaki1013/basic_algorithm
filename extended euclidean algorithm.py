def e_gcd(a, b):
    # 초기화
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        # r
        r = r1 - q * r2
        r1 = r2
        r2 = r
        # s
        s = s1 - q * s2
        s1 = s2
        s2 = s
        # t
        t = t1 - q * t2
        t1 = t2
        t2 = t
    return r1, s1, t1