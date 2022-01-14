# BOJ 20040 : 사이클 감지
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)


def find(a):
    if p[a] != a:
        p[a] = find(p[a])  # 경로 압축 쓰임
    return p[a]


def union(a, b):
    p[find(a)] = find(b)


# 개수까지 카운트 (BOJ 4195)
# def union(a, b):
#     a, b = find(a), find(b)
#     if a != b:
#         p[a] = b
#         temp = number[a] + number[b]
#         number[a], number[b] = temp, temp

n = int(input())
p = [i for i in range(n)]
number = dict()
for i in range(n):
    number[i] = 1
