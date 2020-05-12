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
# 1874      스택 수열
# 
# basic time complexity = o(n) * o(n * 2)
###########################################
class StackNumber1874:

    # listStack : <p> 리스트 팝업과 배열 검증을 위한 함수 </p>
    #     @return nl:array 확인할 수열
    #
    # run : <p> 알고리즘을 확인을 위한 테스트 </p>

    def listStack(self, nl):

        s = len(nl)
        l = [1 for i in range(s)] # 배열 검증을 위하여 수열과 같은 크기의 배열 선언 및 초기값(1) 할당
        n = [1 for i in range(s * 2)] # 리스트 팝업을 위하여 2(push, pop) * n 만큼의 크기의 배열 선언
        p = 0 # 배열 검증을 위한 포지션
        m = 0 # 리스트 팝업을 휘한 포지션

        for i in nl:

            if p > i: # 수열의 이전 수가 현재수 보다 클 경우

                for u in range(i, p-1): # 현재 포지션에서 이전 포지션을 순회 하며 수열 검증

                    if l[u] == 1: # [1, 1, 1(i), 1(u), 0(p)]일 경우 'NO'출력

                        return print('NO')

            else: # 현재수가 클 경우이므로 이전수에서 부터 현재 수까지 push(+) 처리

                for u in range(p, i):

                    if l[u] == 1: # [1, 1, 1, 0(p), 0(pass), 1(+), 1(+, i)] 처리 및 리스트 팝업 길이 증가

                        n[m] = '+'
                        m = m + 1

            n[m] = '-' # 현재 수를 찾았으니 pop(-)처리
            m = m + 1 # 리스트 팝업 길이 증가
            p = i # 이전 포지션 > 다음 포지션으로 이동
            l[p-1] = 0 # 포지션 처리를 종료 하였으므로 0 변환

        for u in n:
            print(u)

    def run(self):
        r = int(read())
        
        l = [int(read()) for v in range(r)]

        self.listStack(l)

# test asseting
util.run([
    StackNumber1874()
])