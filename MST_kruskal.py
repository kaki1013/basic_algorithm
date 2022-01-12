# 1197 풀이: https://www.acmicpc.net/source/share/03ced5904c3a4d4ea16b9db00e55587e
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def find(a):
    if p[a] != a:
        p[a] = find(p[a])   # 경로 압축 쓰임
    return p[a]


def union(a, b):
    p[find(a)] = find(b)


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = [i for i in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))

    # Kruskal's algorithm
    edges.sort()
    count = 0
    MST = 0
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            MST += w
            count += 1
        if count == n - 1:
            break
    print(MST)
