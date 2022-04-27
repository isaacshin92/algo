#V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
#특정한 두 개의 노드에 경로가 존재하는지 확인
#두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력
import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    stack = []
    visited_list = [False] *(V + 1)
    
    stack.append(start)
    
    while stack:
        v = stack.pop()
        visited_list[v] = True
        for w in range(V + 1):
            if not visited_list[w]:
                if arr[v][w]:
                    stack.append(w)
    return visited_list[end]

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int,input().split())
    
    arr = []
    for i in range(V + 1):
        arr.append([0] * (V + 1))
    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1
    start, end = map(int, input().split())
    
    result = 1
    
    if not dfs(start, end):
        result = 0
    
    print(f"#{test_case} {result}")
    