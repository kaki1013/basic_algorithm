# 1197 풀이: https://www.acmicpc.net/source/share/6114c880a073475e80c7da1f03150562
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize   # 2147483647


def Prim(s):
    found = [False] * V
    min_weight = [INF] * V
    sum_weight = 0
    min_weight[s] = 0
    hq = [(0, s)]
    while len(hq) > 0:
        weight, u = heapq.heappop(hq)
        if found[u]: continue
        found[u] = True
        sum_weight += weight
        for v, w in adj[u]:
            if min_weight[v] > w:
                min_weight[v] = w
                heapq.heappush(hq, (min_weight[v], v))
    return sum_weight


if __name__ == "__main__":
    V, E = map(int, input().split())
    adj = [list() for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u - 1].append((v - 1, w))
        adj[v - 1].append((u - 1, w))

    MST = Prim(0)
    print(MST)