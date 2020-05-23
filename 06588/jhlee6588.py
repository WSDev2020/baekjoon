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
# 6588      골드바흐의 추측
# 
# basic time complexity = o(n^n)
###########################################
class Goldbach6588:

    dic = {}

    def isSingleDecimal(self, n):

        # 홀수의 경우
        if n % 2 == 0:
            return False

        # 딕셔너리에 저장 되어 있는 값
        if n in self.dic:
            return self.dic[n]

        # 소수 확인
        for v in range(2,n):
            if n % v == 0:
                return False
        
        # 소수일 경우 딕셔너리에 캐싱
        self.dic[n] = True

        return self.dic[n]

    def nextSingleDecimal(self, n, m):

        for v in range(n+1,1000000):

            if v % 2 != 0:

                if self.isSingleDecimal(v):

                    return v

        return -1

    def run(self):

        init = 3

        while(True):
            
            n = int(read())

            if(n == 0):
                break

            d1 = init

            while(True):

                d2 = n - d1

                if(self.isSingleDecimal(d2)):
                    print("{0} = {1} + {2}".format(n, d1, d2))
                    break
                    
                d1 = self.nextSingleDecimal(d1, n)

                if(d1 < 0)
                    break



# test asseting
util.run([
    Goldbach6588()
])

