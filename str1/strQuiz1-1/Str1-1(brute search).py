#문자열 비교 실행 시간 : 0.11678s
#  Brute Search 
import sys 

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    str = input()
    target = input()
    
    result = 0
    index = len(str) - 1
    str_index = len(str) 
    
        
    for i in range(len(target) - len(str) -1):
        if target[i:i+len(str)] == str:
            result = 1
        
    print(f"#{test_case} {result}")
    
    
    
    # while index < len(target) - 1:
        # if target[index] != str[str_index - 1]:
        #     print(f"index : {index}")
        #     print(f"str_index : {str_index -1 }")
            
        #     print("if >>>")
        #     print(f"target[index] : {target[index]}")
        #     print(f"str[str_index] : {str[str_index - 1]}")
        #     index += str_index   # moving on to next index
        #     str_index = len(str) - 1 #reset
            
        #     if str_index < 0:
        #         result = 1
        #         break
        #     elif index >= len(target):
        #         result = 0 
        #         break
        # else:
        #     print("else >>>")
        #     print(f"target[index] : {target[index]}")
        #     print(f"str[str_index] : {str[str_index]}")
        #     str_index -= 1
        #     index -= 1
        


    
    # for i in range(1, len(target) - len(str) + 1):
        # if target[index] != str[len(str) - 1]: #마지막자리가 틀린 경우로, index에 찾는 문자열의 길이만큼 더해준다. 
        #     print(f"다름 {target[index]} / {str[len(str) - 1]}")
        #     index += len(str) 
        #     print(f"index check : {index}")
        # else:
        #     print("같네")
        #     print(f"같네 {target[index]} / {str[len(str) - 1]}")