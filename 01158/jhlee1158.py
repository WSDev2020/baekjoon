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
# 1158      요세푸스
# 
# basic time complexity = o(n)
###########################################
class Josephus1158:

    repo = None
    rpof = []

    def josephus(self, k, n):

        ac = n
        ap = n

        self.repo = [v+1 for v in range(k)]

        while(len(self.repo) > 0): #배열 순환
            
            if ac == n: # n(x) 일 경우 배열 이동

                ap = ap - 1 # appointment를 한칸 아래로 이동(배열을 위한 인덱싱 처리)

                self.rpof.append(str(self.repo[ap])) # repository의 값을 repo forward로 이동

                del self.repo[ap] # respotiroy의 값 제거

            ac = 1 if ac == n else ac + 1 ## n값이 최대일 경우 처리
            ap = 1 if ap >= len(self.repo) else ap + 1 ## k값에 만날 경우 처리

        print("<{0}>".format(','.join(self.rpof)))

    def run(self):

        k, n = [int(v) for v in input().split()]
        self.josephus(k, n)

# test asseting
util.run([
    Josephus1158()
])