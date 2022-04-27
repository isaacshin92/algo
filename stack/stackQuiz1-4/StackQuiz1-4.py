
import sys


sys.stdin = open("input.txt")

def duplicateChecker(letter):
    v = result.pop()
    if v == letter:
        return
    else:
        result.append(v)
        result.append(letter)

T = int(input())

for test_case in range(1, T + 1):
    test_str = input()
    
    result = []
    
    for i in range(0, len(test_str) ) :
        if len(result) <= 0 :
            result.append(test_str[i])
            # print(f"Before duplicateChecker {result}")
        elif len(result) > 0:    
            duplicateChecker(test_str[i])
            # print(f"After duplicateChecker {result}")
    print(f"#{test_case} {len(result)}")
    