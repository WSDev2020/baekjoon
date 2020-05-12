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
# 9012      괄호
# 
# basic time complexity = o(n)
###########################################
class Bracket9012:

    # bracket : <p> 괄호의 VPS여부를 확인하는 함수 </p>
    #     @return w:str 확인할 문자열
    #
    # run : <p> 알고리즘을 확인을 위한 테스트 </p>

    def bracket(self, w):

        m = len(w)
        r = 0 # 검증을 위하여 초기화 포지션(0) 할당
        for i in range(m):

            c = w[i]

            if c == '(': # VPS 시작 지점
                r = r + 1
            elif c == ')': # VPS 종료 지정
                if r == 0: return 0 # VPS가 시작 전 종료 구문이 있을 경우 0처리
                r = r - 1
            else: continue

        return 1 if r == 0 else 0

    def run(self):

        size = int(read())

        for loop in range(size):
            print( 'YES' if self.bracket(read()[:-1]) == 1 else 'NO' )

# test asseting
util.run([
    Bracket9012()
])