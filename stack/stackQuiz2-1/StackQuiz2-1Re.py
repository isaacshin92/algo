
import sys

sys.stdin = open("input.txt")



T = int(input())

for test_case in range(1, T + 1):
    math = list(input().split())
    stack = []
    
    for n in math:
        if n == '.':
            if len(stack) == 1:
                if str(stack[0]).isalpha():
                    print(f'#{test_case} error')
                else:
                    print(f'#{test_case} {stack.pop()}')
            else: 
                print(f'#{test_case} error')
        elif n.isdigit():
            stack.append(n)
        else:
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                b = int(stack.pop())            
                a = int(stack.pop())
                
                if str(a).isalpha() or str(b).isalpha():
                    print(f'#{test_case} error')
                    break
      
                if n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(a - b)
                elif n == '*':
                    stack.append(a * b)
                elif n == '/':
                    stack.append(a / b)
    