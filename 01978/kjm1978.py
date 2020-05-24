from sys import stdin

def remainder(data, divider): # 나머지가 0 이면 true, 아니면 false 반환
    if(data % divider == 0):
        return True
    else:
        return False

def isPrimeNumber(val1):
    if(val1 == 1):          # 1은 소수가 아니므로 False
        return False

    for k in range(2, val1):
        # print("k : " + str(k))
        # print("val1 : " + str(val1))
        if remainder(val1, k):
            return False    # 자기자신 이외에 나누어 지는 수가 있으면 False  
    
    return True

range_ = int(stdin.readline())      # 첫번째 입력에서 몇개의 수를 받을 것인지 정한다.
data = stdin.readline().split()
count = 0

for i in range(range_):

    if(isPrimeNumber(int(data[i]))):
        # print(data[i] + "is PrimeNumber")
        count += 1

print(count)        # 주어진 수들 중 소수의 개수를 출력.


