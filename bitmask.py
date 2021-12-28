"""
#3비트마스크
:정수의 이진수 표현을 통해 상태를 나타내는 자료구조로 사용하는 기법
특히, 비트마스크를 이용한 집합 구현은 가장 대표적이고, 중요한 사례임.

# 비트마스크를 이용한 집합 구현 (출처 및 설명: https://rebro.kr/63)
- 공집합과 꽉 찬 집합 구하기
A = 0; / A = (1 << 10) - 1;
- 원소 추가
A |= (1 << k);
- 원소 삭제
A &= ~(1 << k);
- 원소의 포함 여부 확인
if(A & (1 << k))
- 원소의 토글(toggle)
A ^= (1 << k);
- 두 집합에 대해서 연산
A | B     → A와 B의 합집합
A & B     → A와 B의 교집합
A & (~B)  → A에서 B를 뺀 차집합
A ^ B     → A와 B중 하나에만 포함된 원소들의 집합
- 집합의 크기 구하기
C++(아마?)
int bitCount(int A){
  if(A == 0) return 0;
  return A%2 + bitCount(A / 2);
}
파이썬
def bitCount(x):
    if x == 0:
        return 0
    return x % 2 + bitCount(x // 2)
- 최소 원소 찾기
int first = A & (-A);  # -A = ~A + 1 이기 때문
- 최소 원소 지우기
A &= (A - 1);
- 모든 부분 집합 순회하기
for (int subset = A ; subset ; subset = ((subset - 1) & A)){ }

# 모든 부분집합을 생성하는 생성자 만들기
(출처 및 설명: https://blog.naver.com/PostView.nhn?blogId=kmh03214&logNo=221702095617&parentCategoryNo=&categoryNo=23&viewDate=&isShowPopularPosts=true&from=search)
def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range(1 << len(s)):
        yield [ss for ss,mask in zip(s,masks) if mask & i]
        # yield는 return과는 다르게 generator라는 객체를 만듦, 함수를 호출할 때마다 하나씩 전달

# 부분집합을 구하는 다른 코드
(출처 및 설명: https://itzjamie96.github.io/2020/10/15/python-bitwise-powersets/)
arr = [1,2,3]
n = len(arr)

for case in range(1 << n):
    for element in range(n):
        if case & (1 << element):
            print(arr[element], end=' ')
    print()

# 참고:
https://rebro.kr/63
https://blog.naver.com/PostView.nhn?blogId=kmh03214&logNo=221702095617&parentCategoryNo=&categoryNo=23&viewDate=&isShowPopularPosts=true&from=search
https://itzjamie96.github.io/2020/10/15/python-bitwise-powersets/

# 관련문제:
11723 집합
15650 N과 M(2)
1285

# 팁:
1 << n == 2 ** n
"""