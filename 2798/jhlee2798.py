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
# 2798      블랙잭
# 
# basic time complexity = o^n-1
###########################################
class BlackJeck2798:

    def blackJeck(self):
        n,m = [int(v) for v in input().split()]
        r   = [int(v) for v in input().split()]
        ix  = n - 2 # 3장의 카드 중 2장은 헤아릴 필요가 없으므로 루프에서 제외
        vt  = 0
        
        for v1 in range(ix): # 첫번째 루프 순환 [1],2,3,4
            for v2 in range(v1+1, n): # 두번째 루프 순환 [1,2],3,4 또는 [1],2,[3],4
                for v3 in range(v2+1, n): # 세번째 루프 순환 [1,2,3],4 또는 [1,2],3,[4]

                    rt = r[v1] + r[v2] + r[v3] # 3항목의 합

                    if rt == m : # 최대 값과 동일 할 경우 즉시 반환
                        return m
                    else:
                        if m > rt and rt > vt: # 결과값(rt)이 최대 값(m)을 적을 경우 이전 값(vt)보다 클 경우에 값 변화
                            vt = rt

        return vt

    def run(self):

        print(self.blackJeck())

# test asseting
util.run([
     BlackJeck2798()
])