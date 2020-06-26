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
# 2193      BinaryFriend
# 
# basic time complexity = o^n-c
###########################################
class BinaryFriend2193:

    # 최적화를 위한 키 매핑전략
    d = {}

    def countFriend(self, s, e, n, v):
        
        if s > e:
            return 1

        else:

            # 기존에 등록 된 최적값일 경우 최적값 반환
            if n in self.d and s in self.d[n]:
                return self.d[n][s]            

            else:

                self.d[n] = {}

                r = 0

                if n == 1:
                    r = r + self.countFriend(s+1, e, 0)
                
                else:
                    r = r + self.countFriend(s+1, e, 0)
                    r = r + self.countFriend(s+1, e, 1)

                self.d[n][s] = r

                return r

    def getBinFriend(self, n):

        return self.countFriend(1, n-1, 1)

    def run(self):

        n = int(input())

        m = self.getBinFriend(n)

        print(m)


# test asseting
util.run([
    BinaryFriend2193()
])
