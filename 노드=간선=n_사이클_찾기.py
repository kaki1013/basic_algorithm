# 알고리즘 먼데이 챌린지 3주차 4번 문제 참고
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, prev):
	if vst[v]:  # 이미 방문
		# but 방금 전 노드 아니고(다시 부모 노드 방향 간선 X), 지금 살펴보는 노드가 스택에 존재하고, 답 구하기 전
		if v != stack[-1] and in_stack[v] and not ans:
			# v는 사이클에 존재하는 노드이므로 정답은..
			idx = stack.index(v)
			for i in range(idx, len(stack)):
				ans.append(stack[i]+1)
			return
	else:     # 아직 방문 X
		vst[v] = True
		in_stack[v] = True
		stack.append(v)
		for u in adj[v]:
			if u != prev:
				dfs(u, v)

		in_stack[v] = False
		stack.pop()

N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N):
	u, v = map(int, input().split())
	adj[u-1].append(v-1)
	adj[v-1].append(u-1)

vst = [False] * N
in_stack = [False] * N
stack = []
ans = []

dfs(0, -1)

print(len(ans))
print(*sorted(ans))
