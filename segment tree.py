# 세그먼트 트리란?
# 어떤 배열 데이터에 대허서
#  - 특정 쿼리(누적합, 누적곱, 최댓값, 최솟값 등) : BOJ 2042, 11505, 2357 / 14428: 최솟값의 인덱스로 저장
#  - 배열의 원소를 업데이트하는 연산
# 을 효율적으로 처리하는 트리 자료구조
#
# cf) 세그먼트 트리는 Full Binary Tree(모든 노드가 0개 또는 2개의 자식을 가짐)
#  -> 배열의 길이가 n이면 트리의 높이는 h = ceil(log_2(n)), 노드는 2^(h+1) - 1
#  -> 실제로 구현할 때, 노드의 개수는 4*n개로 설정해도 무관(가장 낭비가 심한 때: n = 2^k + 1 을 2^(k+1)로 생각, 4배하면 충분히 많음)
# ex) 누적합 세그먼트 트리:
#  -> 단말 노드:  배열의 값 자체, 비단말 노드: 두 자식의 합산을 저장

# 아래는 실제 구현
# 해당 index의 노드가 커버(포함)하는 구간 [start, end]
def initialize(index, start, end):
    if start == end:
        nodes[index] = original[start]
        return nodes[index]
    mid = (start + end) // 2
    left = initialize(index * 2, start, mid)
    right = initialize(index * 2 + 1, mid + 1, end)
    nodes[index] = left + right     # min(left, right), max(left, rigtt) 등으로 변형 가능
    return nodes[index]


# 해당 index의 노드가 커버(포함)하는 구간 [nodeStart, nodeEnd]과 질의하는 구간 [reqStart, reqEnd]
def query(index, nodeStart, nodeEnd, reqStart, reqEnd):
    nodeMid = (nodeStart + nodeEnd) // 2
    if reqEnd < nodeStart or nodeEnd < reqStart:
        return 0                    # min은 INF, max는 -INF 등 '영향을 주지 않는 값'으로 변형 가능
    elif reqStart <= nodeStart and nodeEnd <= reqEnd:
        return nodes[index]
    else:
        left = query(index * 2, nodeStart, nodeMid, reqStart, reqEnd)
        right = query(index * 2 + 1, nodeMid + 1, nodeEnd, reqStart, reqEnd)
        return left + right         # min(left, right), max(left, rigtt) 등으로 변형 가능


# 해당 index의 노드가 커버(포함)하는 구간 [nodeStart, nodeEnd]과 업데이트하는 노드의 인덱스와 값 reqIndex, newVal
def update(index, nodeStart, nodeEnd, reqIndex, newVal):
    nodeMid = (nodeStart + nodeEnd) // 2
    if nodeStart == nodeEnd:
        nodes[index] = newVal
    else:
        if reqIndex <= nodeMid:
            update(index * 2, nodeStart, nodeMid, reqIndex, newVal)
        else:
            update(index * 2 + 1, nodeMid + 1, nodeEnd, reqIndex, newVal)
        nodes[index] = nodes[index * 2] + nodes[index * 2 + 1]  # min(left, right), max(left, rigtt) 등으로 변형 가능


# test_program
size = 8
original = [1, 2, 3, 4, 5, 6, 7, 8]
nodes = [0] * (4 * size)

initialize(1, 0, size - 1)

for _ in range(int(input('test num : _\b'))):
    q = int(input('1 query, 2 update : '))
    if q == 1:
        arg = map(int, input('어디부터 어디를 (0~7) : ').split())
        print(query(1, 0, 7, *arg))
    if q == 2:
        arg = map(int, input('어디를 몇으로? : ').split())
        update(1, 0, 7, *arg)
        print(nodes)
    print()