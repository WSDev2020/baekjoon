#! python3
# -*- coding: utf-8 -*- 
import sys # system module
import math as Math

###########################################
# 유틸성 함수 묶음
###########################################
class Utils:
    # isUnary : <p> 단항 연산자 여부를 반환하며 단항 일 경우 1 그외에는 0을 반환 </p>
    #     @return r:int 단항 연산자 여부
    #
    # isBinary : <p> 이항 연산자 여부를 반환하며 이항 일 경우 1 그외에는 0을 반환 </p>
    #     @return r:int 단항 연산자 여부
    #
    # run : <p> 코드 실행을 위한 추상화 함수 </p>
    #     @param runLst:array 코드 묶음

    def isUnary(self, e):

        return 1 if len(e) == 1 else 0
    
    def isBinary(self, e):

        return 1 if len(e) == 2 else 0

    def run(self,runLst):
        for r in runLst :
            r.run()

# 함수 초기화 처리
read = sys.stdin.readline
util = Utils()

###########################################
# no        title
# 10872     팩토리얼
# 
# basic time complexity = o(n)
###########################################
class Factorial10872:

    def factorial(self, n):
        
        return n * self.factorial(n -1) if n > 1 else 1

    def run(self):

        print(self.factorial(int(input())))

class Fibonacci10870:
    def fibonacci(self, n):

        if n == 0: return print(0) # 0일 경우
        if n == 1: return print(1) # 1일 경우

        r = 0
        p = 1
        v = p

        for i in range(n-1):
            v = r + p
            r = p
            p = v

        print(p)

    def run(self):

        self.fibonacci(int(input()))

# test asseting
util.run([
    Factorial10872()
])