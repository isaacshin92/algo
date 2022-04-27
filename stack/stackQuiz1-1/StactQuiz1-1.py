# 가로x세로 길이가 10x20, 20x20인 직사각형
# 20xN 크기 안에 준비한 종이를 빈틈없이 붙이는 방법
# 10의 배수인 N이 주어졌을 때, 
# 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산
# 직사각형 종이가 모자라는 경우는 없다.
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수
import sys 

def cnt(N):
    arr = []
    
    if N == 1:
        return 1 
    elif N == 2:
        return 3
    else:
        arr.append(cnt(N-1) + cnt(N-2) *2)
    return arr[-1]
    
def memoCnt(N):
    m = [0] * (N + 1)
    m[0] = 1
    m[1] = 1
    
    for i in range(2, N + 1):
        m[i] = m[i-1] + m[i-2] *2
    # print(m)
    return m[-1]




# sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # print(f"#{test_case} {cnt(N//10)}")
    
    print(f"#{test_case} {memoCnt(N//10)}")
    