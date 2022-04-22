
import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    
    k, n, m  = list(map(int, input().split())) #입력 예 ) 3 10 5 최대거리, 정류장 수, 충전기 있는 정류소 숫자 
    chrg= list(map(int, input().split())) #충전기가 설치된 정류장 
    
    max_charge = k #버스가 한번에 갈 수 있는 최대 거리 
    arr = n #총 정류소 크기
    charger_stop_cnt = m
    count = 0
    now = 0
    nowK = 0 + k
    
    bus_stop = list(range(0, n + 1))
    # print(bus_stop)
    # print(chrg)
    
    for i in chrg:
        bus_stop[i] = 'chrg'
    
    while nowK < n:
        if now == nowK:
            count = 0
            break
        if bus_stop[nowK] == 'chrg': #한번에 갈 수 있는 거리에 충전기가 있는가 ? -> 있으면 일단 거기까지, 이동
            now = nowK #현재 위치 
            nowK = now + k
            count += 1
        elif bus_stop[nowK] != 'chrg':
            nowK -= 1
            

    print(f"#{test_case} {count}")
