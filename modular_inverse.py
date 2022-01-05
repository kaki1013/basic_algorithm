def mod_inverse(a, m):
    # 초기화
    r1, r2 = a, m
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        # r
        temp = r1 - q * r2
        r1 = r2
        r2 = temp
        # s
        temp = s1 - q * s2
        s1 = s2
        s2 = temp
        # t
        temp = t1 - q * t2
        t1 = t2
        t2 = temp
    return s1 % m