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
# 10430     나머지
# 
# basic time complexity = o*4
###########################################
class Remain10430:
    
    def dequeProccess(self):
        n,m,r = read().split()
        n = int(n)
        m = int(m)
        r = int(r)

        print((n+m)%r)
        print(((n%r) + (m%r))%r)
        print((n*m)%r)
        print(((n%r) * (m%r))%r)

    def run(self):

        self.dequeProccess()

# test asseting
util.run([
    Remain10430()
])