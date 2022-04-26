#회문 찾기 
#회문은 1 개만 존재하지만, 가로 뿐 아니라 세로로 존재할 수 있다. 
# 소요시간 
# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.


import sys

sys.stdin = open("input.txt")


# 문자열 슬라이싱  및 비교 함수. 
def reverseCompare(s, n):
    
    result = False
    temp = ''
    
    for i in range(len(s)):
        temp = s[i:n+i+1]
        temp_list = list(temp)
        temp_list.reverse()
        rev = ''.join(temp_list)
        
        print(f"temp : {temp}")
        print(f"rev : {rev}")
        
        if temp == rev:
            return temp
        else:
            return False

T = int(input())

for test_case in range(1, T + 1):
    size, target = map(int, input().split())
    board = []
    verti_board = []
    rlt = ''

    # 빈 리스트에 입력받은 10 X 10 문자열 넣기. 
    for i  in range(size):
        board.append(input())
    for i  in range(size):
        result = reverseCompare(board[i],target)
        
        if result != False:
            rlt = result
      
      
    #새로 리스트 만들기 
    
    for _ in range(size):
        verti_board.append([0]*size)
        
        
    for i in range(0, size):
        for j in range(0, size):
            verti_board[i][j] = board[j][i]
        verti_board[i] = ''.join(verti_board[i])
        
    
    for i  in range(0, size):
        result = reverseCompare(verti_board[i],target)  
        if result != False:
            rlt = result
    
    #최종 결과 출력  
    print(f"#{test_case} {rlt}")
    
    
        
        
    
    

    
