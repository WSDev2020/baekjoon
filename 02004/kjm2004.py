from sys import stdin

# nCm = n!/m!*(n-m)!

'''
1. 문제 그대로 계산하여 0의 개수를 구하니 '시간초과'
2. 0의 개수는 2의개수와 5의 개수 중에서 최소값과 같다는 사실을 이용하여 계산.
'''

def div_number(k, n):   # n 의 개수를 반환 하는 함수.
    count = 0
    while(k != 0):      # n의 개수를 구하기 위해 k에서 n으로 계속 나누어 준다. 
        k = k // n      # // 몫을 구한다.
        count += k      # 몫 만큼이 5의 개수이다. ex) 20/5  = 4  ::=> 5, 10, 15, 20
                        # 제곱수들은 개수를 더 추가해주어야 한다. ex ) 25 = 5 x 5 
                        # 그래서 while 돌면서 몫으로 다시 나누어 줌.
    return count

n, m = list(map(int, input().split()))  # 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.

div_five = div_number(n, 5) - div_number(m, 5) - div_number(n-m, 5) # 5의 개수를 구한다.
div_two = div_number(n, 2) - div_number(m, 2) - div_number(n-m, 2)  # 2의 개수를 구한다. 

print(min(div_five, div_two))   # 2와 5중 최소값을 출력한다.