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
# 1406      에디터
# 
# basic time complexity = o(n)
###########################################
class Editor1406:

    def edit(self):

        lp = list(read().split()[0]) # 초기값 입력
        rp = []

        cs = int(read())

        clist = [read() for c in range(cs)]

        for r in clist:
            cmd = r.split()

            if util.isUnary(cmd):
                r = cmd[0]

                if r == 'L': # 커서를 왼쪽으로 이동
                    if len(lp) > 0:
                        rp.append(lp.pop())
                elif r == 'D': # 커서를 오른쪽으로 이동
                    if len(rp) > 0:
                        lp.append(rp.pop())
                elif r == 'B': # 커서 왼쪽의 문자 삭제 및 커서 문자열 재 설정
                    if len(lp) > 0:
                        del lp[len(lp)-1]
            elif(util.isBinary(cmd)):
                
                r,v = cmd

                if r == 'P':
                    lp.append(v)

        rp.reverse()

        print(''.join(lp + rp))

    def run(self):
        self.edit()

# test asseting
util.run([
    Editor1406()
])