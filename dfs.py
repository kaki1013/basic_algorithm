import sys
sys.setrecursionlimit(10**5)  # 문제 상황에 따라서 조절

# 재귀
def DFS(graph, visited, start):
    if visited[start]:
        return
    visited[start] = True
    for dest in graph[start]:
        DFS(graph, visited, dest)


n, m = list(map(int, input().split()))
s = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
visited = [False for i in range(n+1)]
DFS(graph, visited, s)

# 스택
visited = [False for i in range(n+1)]
stack = [s]
while len(stack) > 0:
    now = stack.pop()
    if visited[now]:
        continue
    visited[now] = True

    for dest in graph[now]:
        if not visited[dest]:
            stack.append(dest)

# 사이클 검사(사이클 구성노드 찾는 건 16947 참고)
def cycle(graph, visited, isInStack, start):
    if isInStack[start]:
        return True
    if visited[start]:
        return False

    visited[start] = True
    isInStack[start] = True

    for dest in graph[start]:
        if cycle(graph, visited, isInStack, dest):
            return True

hasCycle = False
for i in range(1, n+1):
    if not hasCycle:
        hasCycle = cycle(graph, visited, isInStack, start)

print("YES" if hasCycle else "NO")
