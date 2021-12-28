from collections import deque


def bfs(adj, vst, start):
    q = deque([start])
    vst[start] = True

    while q:
        curr = q.popleft()
        for nxt in adj[curr]:
            if not vst[nxt]:
                q.append(nxt)
                vst[nxt] = True
