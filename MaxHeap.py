# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=leeinje66&logNo=221622360256
# maxHeapify 조금 수정
class MaxHeap:
    def __init__(self):
        self.data = [None]  # [None] 에서 삽입 혹은 삭제

    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i] > self.data[(i // 2)]:
                self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
                i = i // 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = 2 * i
        right = (2 * i) + 1
        largest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 부모보다 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[largest] < self.data[left]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            largest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 '부모와 왼쪽 자식 중에서 큰 값'보다 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[largest] < self.data[right]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            largest = right
        if largest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(largest)