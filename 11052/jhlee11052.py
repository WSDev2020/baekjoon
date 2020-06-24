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
# 10844     쉬운 계단 수
# 
# basic time complexity = o^n
###########################################
class EasyStairs10844:

    # 최적화를 위한 키 매핑전략
    d = {}

    def countStairs(self, s, e, n, v):
      
        if s > e:
            return 1
        else:

            # 기존에 등록 된 최적값일 경우 최적값 반환
            if n in self.d and s in self.d[n]:

                return self.d[n][s]
            else:
                self.d[n] = {}

                r = 0

                if n - 1 >= 0:
                    r = r + self.countStairs(s+1, e, n-1, v + str(n-1))
                
                if n + 1 < 10:
                    r = r + self.countStairs(s+1, e, n+1, v + str(n+1))
                
                self.d[n][s] = r

                return r
        

    def findStair(self, n):
        o = 0

        for v in range(1,10):
            o = o + self.countStairs(1, n-1, v, str(v))

        return o

    def run(self):
        n = int(input())
        
        r = self.findStair(n)

        print(r% 1000000000)

# test asseting
util.run([
    EasyStairs10844()
])