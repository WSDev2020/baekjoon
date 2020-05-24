from sys import stdin

data = [int(x) for x in input().strip().split()]

GCD = None # 최대공약수 greatest common divisor
LCM = None # 최소공배수 least common multiple

def remainder(data, divider): # 나머지가 0 이면 true, 아니면 false 반환
    if(data % divider == 0):
        return True
    else:
        return False

first_data = data[0]        # 입력 받은 첫번째 값
second_data = data[1]       # 입력 받은 두번째 값
min_number = first_data if first_data <= second_data else second_data   # 입력 받은 두 수중 작은 수를 담는다.
max_number = second_data if first_data <= second_data else first_data   # 입력 받은 두 수중 큰 수를 담는다.

""" 
# 최대공약수
#   두 수중 크기가 더 작은 수를 기준으로 내려오면서 나눠서 나머지가 둘 다 0이라면 최대공약수로 판단.
"""
for i in range(min_number, 0, -1):  

    if i == 1:
        print(1)
        break

    if remainder(first_data, i) and remainder(second_data, i):
        print(i)
        break

"""
# 최소공배수
"""
for i in range(1, max_number+1):

    if(min_number*i < max_number):     # 작은 수에 i를 곱해서 큰수보다 작다면 아래 로직을 확인할 필요가 없음.
        continue

    if(remainder(min_number*i, max_number)):    # 작은 수에 i를 곱한 값을 큰수로 나누었을때 0이면 공배수이다.
        print(min_number*i)
        break                           # 최소공배수 print하고 break