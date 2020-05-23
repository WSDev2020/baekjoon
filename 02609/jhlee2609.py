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
# 2609      최대공약수와 최소공배수
# 
# basic time complexity = o(n)
###########################################
class GCDAndLCM2609:

    def gcd(self, n, m, r):

        return r if r == 1 or ( n % r == 0 and m % r == 0 ) else self.gcd(n, m, r-1)

    def run(self):

        n, m = [int(v) for v in input().split()]

        n, m = [n, m] if n <= m else [m, n]

        v1 = self.gcd(n, m, n)

        v2 = int( n * m / v1 )
        
        print("{0}\n{1}".format(v1,v2))

# test asseting
util.run([
     GCDAndLCM2609()
])