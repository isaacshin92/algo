# 숫자는 스택에 넣는다.
#연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
#‘.’은 스택에서 숫자를 꺼내 출력한다.
# Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 
# 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

import sys 

sys.stdin = open("input.txt")

def digit_checker(num):
    result = False 
    if num != '+' and num != '-' and num != '*' and num != '/' and num != '.':
        result = True
    return result 


def math_str(l,r,sign):
    l = int(l)
    r = int(r)
    if sign == '+':
        result = l + r
    elif sign == '-':
        result = l - r
    elif sign == '*':
        result = l * r
    else:
        result = l / r
    return result 

def sumDo(i, sign):
    restul = ''
    l = stack[i - 2]
    r = stack[(i - 1)]
    if i >=2 and digit_checker(l) and digit_checker(r):
        result = math_str(l,r,sign)
    elif not digit_checker(l) and not digit_checker(r):
        result = 'error'
    else: 
        result = 'error'
    return result 
    

T = int(input())

for test_case in range(1, T + 1):
    math = list(input().split())
    stack = []
    rlt = ''
    # print(f'math : {math}')
    
    for i in range(len(math)): #숫자일 때 

        if math[i] == '.':
            if len(stack) == 1:
                if digit_checker(stack[0]):
                  print(f'#{test_case} {stack[0]}')
                  break
                else:
                   print(f'#{test_case} error') 
            else:
                print(f'#{test_case} error') 
        if math[i] != '+' and math[i] != '-' and math[i] != '*' and math[i] != '/' and math[i] != '.':
            stack.append(math[i])
            
        else: # 기호일 때 
            rlt = sumDo(len(stack), math[i])
            
            if rlt == 'error':
                print(f'#{test_case} {rlt}')
                break
            
            stack.pop()
            stack.pop()
            stack.append(rlt)


            