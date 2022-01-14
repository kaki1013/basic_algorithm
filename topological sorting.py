# 아래 예시 코드의 문제 : BOJ 2252
# DP + Topological Sort : 작업 (BOJ 2056), ACM Craft (BOJ 1005)
# 정렬 불가능 판별: 음악프로그램 (BOJ 2623)
"""
# 위상 정렬
- 의존성이 있는 작업들이 주어질 때, 수행해야 하는 순서
- 유향 그래프의 정점을 방향을 거스르지 않도록 나열하는 것 (유향 그래프의 정점을 정렬하는 것)
    “간선 (i, j)가 존재하면 정렬 결과에서 정점 i는 반드시 정점 j보다 앞에 위치해야 한다.”
cf. 정렬할 그래프 = 유향 비순환 그래프, DAG(Directed Acyclic Graph)

# 라이브러리
참고: https://docs.python.org/ko/3/library/graphlib.html
graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
ts = TopologicalSorter(graph)
tuple(ts.static_order())
-> ('A', 'C', 'B', 'D')

# pseudo code
for i ← 1 to n {
    진입 간선이 없는 정점 u를 선택한다.
    A[i] = u
    정점 u와 u의 진출 간선을 모두 제거한다.
}
return A[]

# 구현
1. bfs - queue, “진입 간선이 없는 정점을 선택하고 제거한다”
result = List()
while (Q is not empty)
    u = Q.pop()
    result.push(u)
    for (u에 인접한 정점 v에 대해서)
        INDEGREE[v] -= 1
        if (INDEGREE[v] == 0)
            Q.push(v)
return result

2. dfs - 종료 순서를 뒤집기만 하면 됨
    -> 정당성: 귀류법으로 가능 (참고: 알고리즘 문제 해결 전략 831페이지를 참고)
            어떤 간선 (u, v) 에 대해서, dfs로 얻어낸 위상 정렬의 결과에서 (v, u)가 있다고 가정
            즉 dfs(u)가 종료 후, dfs(v)가 종료됨 & dfs(u)는 종료되기 전에 간선 (u, v)를 검사함
            dfs(u) 에서
            1. vst[v] 가 거짓: dfs(v)를 재귀 호출하면서, dfs(v)가 먼저 종료됐을 것임 =><=
            2. vst[v] 가 참:  dfs(v) 가 먼저 호출됐다는 뜻 + dfs(v)가 나중에 종료되었음
                            즉 dfs(v)는 실행 중이고 dfs(u)를 재귀호출 한 것임
                            간선 (v, u)가 존재한다는 의미 -> 사이클 존재 =><=

DFS(u) {
    visited[u] = True
    for (u에 인접한 정점 v에 대해서)
        if (visited[v] = False) DFS(v)
    result.push(u)
}

result = List()
for (모든 정점 u에 대해서)
    visited[u] = False
for (모든 정점 u에 대해서)
    if (visited[u] = False) DFS(u)
reverse(result) // result 를 뒤집는다.
return result

# 최단거리에서의 응용 (참고 : https://ko.wikipedia.org/wiki/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC)
-> 위상 배치는 역시 길이의 DAG를 통해서 최단 거리를 빠르게 계산하는데 사용된다. V를 토폴로지 순서로 이러한 그래프의 정점 목록이라고 하자.
1. d를 V와 같은 길이의 배열이라고 하자. 이것은 s에서 최단 경로 거리를 유지한다.
    d[s] = 0, d[u] = INF
2. p를 V와 동일한 길이의 배열로, 모든 요소는 nil로 초기화한다. 각 p[u]는 s에서 u까지의 최단 경로에서 u의 선행자를 보유한다.
3. s에서 시작하여 V에서 순서대로 정점 u를 반복한다. :
    u 바로 뒤에 오는 각 꼭짓점 v에 대해 (즉, u에서 v까지의 간선이 존재한다.):
        w를 u에서 v까지의 간선의 가중치라고 하자.
        가장자리를 풀다. : if d[v] > d[u] + w, set
            d[v] ← d[u] + w,
            p[v] ← u.

# 정렬 불가능 판별: BOJ 2623
-> 정렬이 가능한 것과 결과가 N개인 것은 필요충분조건
"""
# 참고: https://www.acmicpc.net/source/share/e6f76e4167714f60852b3cf559aaefad 을 정리
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    in_degree = [0] * N
    adj = [list() for _ in range(N)]

    # 1. 각 정점마다 진입 간선의 수를 INDEGREE에 저장한다.
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        in_degree[v - 1] += 1

    # 2. 진입 간선이 없는 정점(INDEGREE[i] == 0)을 모두 queue에 넣는다.
    queue = deque()
    for u in range(N):
        if in_degree[u] == 0:
            queue.append(u)

    # Topological Sorting
    result = []
    while queue:
        u = queue.popleft()
        result.append(u+1)

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # 출력
    print(*result)

# 참고: http://boj.kr/1db6303b1a6a47c48abc2723cf2b7cd9
import sys
sys.setrecursionlimit(10**9)

def int_input():
    text = sys.stdin.readline()
    return int(text)

def intlist_input():
    str_values = sys.stdin.readline().split()
    return map(int, str_values)

def DFS_TS(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            DFS_TS(v)
    result.append(u)

if __name__ == "__main__":
    N, M = intlist_input()
    adj = [list() for _ in range(N)]
    for _ in range(M):
        u, v = intlist_input()
        adj[u - 1].append(v - 1)

    visited = [False] * N
    result = []
    for u in range(N):
        if not visited[u]:
            DFS_TS(u)

    result.reverse()

    for u in result:
        print(u + 1, end=' ')