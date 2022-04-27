#괄호 {}, ()가 제대로 짝을 이뤘는지 검사 
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력

import sys

def matchUp(my_str):
    temp = []
    cnt = 0
    result = int()

    # (),{} 만 리스트에 추가.
    for i in my_str:
        
        if i == '(' or i == '{':
            temp.append(i)
            # print(f"temp : {temp}")
        elif i == ')' or i == '}':
            
            #처음부터 닫는 괄호가 나온 경우 체크
            if len(temp) == 0:
                result = 0
                break
            
            # 마지막 요소와 짝이 맞지 않는 경우 체크 
            elif i == ")" and temp[-1] == '{' or i == '}' and temp[-1] == '(':
                result = 0
                break
            
            else:
                temp.pop()
                if len(temp) == 0:
                    result = 1
            # print(f"temp : {temp}")

                
    return result



sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    my_str = list(input())
    
    print(f"#{test_case} {matchUp(my_str)}")
    

    