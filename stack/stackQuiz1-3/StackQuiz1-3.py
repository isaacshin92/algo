#V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
#특정한 두 개의 노드에 경로가 존재하는지 확인
#두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력
#

# import sys

# sys.stdin = open("input.txt")

# T = int(input())

# for test_case in range(1, T + 1):
#     node, edge = map(int, input().split())

#     edge_list = [[0,0]]
#     stack  = []
#     visite_list = [0] * (node + 1) # 방문여부: 방문시 -> 1
#     cur_node = 1
#     next_node = 0

#     #node 연결 정보
#     for i in range(edge):
#         temp = list(map(int,input().split()))
#         edge_list.append(temp)
#         edge_list.sort()

#     #찾고자 하는 경로의 시작과 끝 
#     start, end = map(int,input().split())
    
#     for _ in range(node):
#         visite_list[cur_node] += 1
#         next_node = edge_list[cur_node - 1][1]
        
#         if visite_list[next_node] == 0:
#             cur_node = next_node
#         elif visite_list[next_node] == 1:
#             cur_node = 1
            
#         if cur_node == end:
#             result = 1
#             break

import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    stack = []
    visit = [False] * (V+1)
    stack.append(start)
    # 입력받은 start부터 시작, 값이 있고 아직 방문하지 않은 정점이면 stack에 추가
    while stack:
        v = stack.pop()
        visit[v]=True
        for w in range(V+1):
            if not visit[w]:
                if arr[v][w]:
                    stack.append(w)
    # end 지점을 방문하였는지 반환
    return visit[end]


#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    #정점과 간선의 개수 입력
    V, E = map(int,input().split())
    arr = [[0] *(V+1) for _ in range(V+1)]
    #arr에 입력받은 연결된 정점 표시
    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1
        # print(arr)
    result = 1
    #입력받은 a가 b에 연결되어있는지 확인
    a, b= map(int,input().split())
    if not dfs(a,b):
        result = 0
    print('#{} {}'.format(tc, result))       

    
