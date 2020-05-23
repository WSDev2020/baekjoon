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
    #
    # reduce : <p> 전방위로 탐색하면서 값을 증가/감을 처리한다</p>
    #     @param l:Array 탐색 시 사용 할 리스트
    #     @param f:Function 탐색 시 처리 할 함수
    #     @param i:Object 초기 값

    def isUnary(self, e):

        return 1 if len(e) == 1 else 0
    
    def isBinary(self, e):

        return 1 if len(e) == 2 else 0

    def run(self,runLst):
        for r in runLst :
            r.run()

    def reduce(self, l, f, i):
        
        v1 = i
        v2 = [v for v in l]
        
        for v in v2 :
            v1 = f(v2, v, v1)
        
        return v1    

# 함수 초기화 처리
read = sys.stdin.readline
util = Utils()

###########################################
# no        title
# 1978      소수 찾기
# 
# basic time complexity = o(n)-1
###########################################
class FindDecimal1978:

    def run(self):

        n = int(input())

        l = [int(v) for v in input().split()]

        r = util.reduce(l, self.callback, 0)

        print(r)

    def callback(self, l, v, i):
        e = True
        
        if v == 1:
            return i

        for v1 in range(2, v):
            if v % v1 == 0:
                e = False
                break

        return i + 1 if e else i

# test asseting
util.run([
    FindDecimal1978()
])