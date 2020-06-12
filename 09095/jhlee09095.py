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
# 09095     1,2,3 더하기
# 
# basic time complexity = o^n3
###########################################
class Addition123Number9095:

    # 최적화를 위한 키 매핑전략
    d = {-3 : 0, -2 : 0, -1 : 0, 0 : 1, 1 : 1, 2 : 2}

    def addN(self, n):
        
        if n in self.d :
            return self.d[n]

        self.d[n] = self.addN(n-1) + self.addN(n-2) + self.addN(n-3)

        return int(self.addN(n))

    def run(self):
        c = int(input())
        l = [0 for v in range(c)]

        for n1 in range(c):
            l[n1] = str(self.addN(int(input())))

        print("\n".join(l))

# test asseting
util.run([
    Addition123Number09095()
])