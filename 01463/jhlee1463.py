#! python3
# -*- coding: utf-8 -*- 
import sys # system module
import math as Math

###########################################
# 추가 된 부분
###########################################
# Make1No1463
# N2tiling11726

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

    def run(self, runLst):
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
# 1463      1로 만들기
# 
# basic time complexity = o(n)
###########################################
class Make1No1463:

    # 최적화를 위한 키 매핑전략
    d = {1 : 0, 2 : 1, 3 : 1 }
    
    def findNum(self, n):
        
        v1 = -1
        v2 = -1
        v3 = sys.maxsize

        # 기존에 등록 된 최적값일 경우 최적값 반환
        if n in self.d:
            return self.d[n]

        # n으로 나눌수 있을 경우 n으로 분해
        v1 = 1 + self.findNum(n / 3) if n % 3 == 0 else v3
        v2 = 1 + self.findNum(n / 2) if n % 2 == 0 else v3

        # n으로 나누어 지지 않을 경우 -1로 기능도 분해
        if v1 == v3 or v2 == v3:
            v3 = 1 + self.findNum(n - 1)

        # 최적화를 위한 임시 값 등록
        self.d[n] = v3 if ( v3 <= v2 and v3 <= v1 ) else v2 if ( v2 <= v1 and v2 <= v3 ) else v1

        return self.d[n]

    def run(self):
        n = int(input())

        r = self.findNum(n)

        print(r)

# test asseting
util.run([
    Make1No1463()
])
