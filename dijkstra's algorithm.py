# 알림_2020여름방학 정규세미나 6주차_최단경로 참고_다익스트라
# http://boj.kr/e791640f89d649adbb6fabe51f196fd5
import heapq
import sys

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

# weight := 가중치 인접 리스트 (from u to v)
weight = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    weight[u].append((v, w))
priority_queue = []
distance = [10**6 for _ in range(V+1)]
found = [False for _ in range(V+1)]

distance[K] = 0
heapq.heappush(priority_queue, (0, K))  # (거리, 정점번호)

while priority_queue:
    _, u = heapq.heappop(priority_queue)
    if found[u]:
        continue
    found[u] = True
    for v, w in weight[u]:
        if distance[v] > distance[u] + w:
            distance[v] = distance[u] + w
            heapq.heappush(priority_queue, (distance[v], v))

for i in range(V):
    d = distance[i+1]
    if d == 10**6:
        print("INF")
    else:
        print(d)
