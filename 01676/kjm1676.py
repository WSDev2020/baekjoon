from sys import stdin

class Factorial:
    number = 0
    rtn = 1

    def __init__(self, number):
        self.number = number

    def get(self):
        for i in range(self.number, 1, -1):
            self.rtn *= i

        return self.rtn

data = Factorial(int(stdin.readline())) # factorial을 계산할 input을 받는다.
factorial = str(data.get())[::-1]       # factorial 결과값을 reverse해서 저장. for in 문자열 을 사용하기 위함.
count = 0                               # 0의 개수를 count하는 변수 선언.

for s in factorial:
    if(s) != '0':
        print(count)        # 0이 아니면 문제에서 요구한대로 0의 개수를 출력한다.
        break
    count += 1              # 0의 개수를 count 한다. 
