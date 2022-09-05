def coprime(n):
    ans = n

    p = []
    i = 2
    while i <= int(n**0.5)+1:
        if n % i == 0:
            p.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n != 1:
        p.append(n)
    
    
    for pp in p:
        ans = ans // pp * (pp-1)
    return ans
