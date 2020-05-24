from sys import stdin

def isPrime(n):
    numbers=[1]*n 

    for i in range(2, int(n**0.5)+1):   # 주어진 수에서 판단해야 할 범위는 n의 루트 개 만큼만 판단하면 된다.
        if numbers[i]==1:
            for j in range(i+i,n,i):
                numbers[j]=0
    return numbers

numbers=isPrime(10)    # 문제에서 테스트 수는 1,000,000를 넘지 않는다고 했으므로 미리 소수를 구해둔다.

while True:
    n=int(input())
    if n==0:
        break
    for i in range(3, n//2+1):
        if numbers[i] and numbers[n-i]:     # 두 수가 모두 소수이면 주어진 format으로 출력
            print("{} = {} + {}".format(n,i,n-i))
            break

"""
# 2. PrimeList를 data 입력받을때마다 만드는 방법. 시간초과
# 3. 2번 방법이 시간초과가 나와서 주어진 100,000개의 소수를 미리 구해두고 해볼려고 시도
# 4. 에라토스테네스의 체 방법을 사용. 

def remainder(data, divider): # 나머지가 0 이면 true, 아니면 false 반환
    if(data % divider == 0):
        return True
    else:
        return False

def isPrimeNumber(val1):
    if(val1 == 1):          # 1은 소수가 아니므로 False
        return False

    for k in range(2, val1):
        if remainder(val1, k):
            return False      # 자기자신 이외에 나누어 지는 수가 있으면 False  
    
    return True

def PrimeNumberList(val1):
    primeList = [1]*val1

    for m in range(2, int(val1)):
        if(isPrimeNumber(m)):
            primeList.append(m)

    return primeList

# data에 해당하는 PrimeNumber List를 미리 만들고 비교
primeList = PrimeNumberList(50000)
print("-----")
while(True):
    data = int(stdin.readline())

    if(data == 0):
        break

    for i in range(2, int(data/2)):
        if(i in primeList and data-i in primeList):
            print("{} = {} + {}".format(data, i, data-i))
            break
"""

"""
    # 1. 시간초과로 미리 list에 PrimeNumber를 담아서 비교하는 방법으로 변경
    breaker = False # 이중 loop를 벗어나기 위한 변수 선언       
    for i in range(data-1, 0, -2):  # 주어진 문제에서 두 홀수의 합이라고 했으므로 -2씩 내려가면 된다.
        if(breaker == True):
                break
        if(isPrimeNumber(i)):
            if(breaker == True):
                break
            for k in range(1, data//2, 2):     # 주어진 값에서 1/2만큼만 돌면된다. 주어진 문제에서 i + k = data 이므로.
                if(isPrimeNumber(k) and i+k == data):
                    print(str(data) + " = " + str(k) + " + " + str(i))
                    breaker = True
                    break
"""        

    