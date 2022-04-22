
import sys

sys.stdin = open('input.txt')

T = int(input())


for test_case in range(1, T + 1):
    
    card_num = int(input())
    card_list = list(input())
    card_list.sort()

    count = 0
    
    for i in card_list:
        if count < card_list.count(i):
            count = card_list.count(i)
            card  = i
        elif count == card_list.count(i):
            card = i
        
    print(f"#{test_case} {card} {count}")