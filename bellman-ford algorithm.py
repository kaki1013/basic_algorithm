# 알림_2020여름방학 정규세미나 6주차_최단경로 참고_벨만-포드
TC = int(input())
for _ in range(TC):

    # input
    N, M, W = map(int, input().split())
    weight = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        weight.append((S, E, T))
        weight.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        weight.append((S, E, -T))

    # Bellman-Ford
    distance = [10 ** 7] * (N + 1)
    distance[1] = 0
    for _ in range(N-1):
        for u, v, w in weight:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    previous = distance[:]
    for u, v, w in weight:
        if distance[v] > distance[u] + w:
            distance[v] = distance[u] + w

    for i in range(N+1):
        if previous[i] != distance[i]:
            print('YES')
            break
        if i == N:
            print('NO')
            break
