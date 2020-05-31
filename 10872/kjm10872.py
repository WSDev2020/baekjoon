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

data = Factorial(int(stdin.readline()))     # factorial을 계산할 input을 받는다.
print(data.get())