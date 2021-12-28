# 알림_2020여름방학 정규세미나 6주차_최단경로 참고_플로이드-워샬
import sys

# 입력
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

dist = [[10**9 for _ in range(n)] for _ in range(n)]

# 초기화
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
for i in range(n):
    dist[i][i] = 0

# 플로이드-워샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 불가능한 경우 0으로 수정
for i in range(n):
    for j in range(n):
        if dist[i][j] == 10**9:
            dist[i][j] = 0

# 출력
for line in dist:
    print(*line)
