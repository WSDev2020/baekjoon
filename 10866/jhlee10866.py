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
# 10866     덱(데크)
# 
# basic time complexity = o(n)^r
###########################################
class Deque:

    # __init__ : <p>생성자</p>
    #     @param size:int 초기배열 사이즈
    #
    # push_back : <p>값을 배열의 끝 부분에 추가 하는 함수</p>
    #     @param e:object 등록 할 값
    #
    # push_front : <p>값을 배열의 앞 부분에 추가 하는 함수</p>
    #     @param e:object 등록 할 값
    #
    # pop_front : <p>배열의 처음 값을 추출 하는 함수</p>
    #     @return r:str 배열의 마지막 값
    # 
    # pop_back : <p>배열의 마지막 값을 추출 하는 함수</p>
    #     @return r:str 배열의 마지막 값
    #
    # size : <p>배열의 사이즈(길이)를 반환하는 함수</p>
    #     @return r:int 배열의 길이
    #
    # empty : <p>배열이 비어 있을 경우 -1 비어 있지 않을 경우 1을 반환하는 함수</p>
    #     @return r:int 배열의 길이 검증 값
    #
    # front : <p>덱의 가장 앞에 있는 엘리먼트를 반환(엘리먼트 삭제 X)</p>
    #     @return r:int 배열의 가장앞에 있는 엘리먼트
    #
    # back : <p>덱의 가장 뒤에 있는 엘리먼트를 반환(엘리먼트 삭제 X)</p>
    #     @return r:int 배열의 가장뒤에 있는 엘리먼트

    repo = None
    hwm = 0
    lwm = 0
    
    def __init__(self, *size):
        self.repo = [0 for i in range(0 if len(size) == 0 else int(size[0]))]

    def push_back(self, e):
        self.repo[self.hwm] = e
        self.hwm = self.hwm+1

    def push_front(self, e):

        if(self.lwm == 0):
            self.repo = [e] + self.repo
            self.hwm = self.hwm + 1
        else:
            self.lwm = self.lwm - 1
            self.repo[self.lwm] = e

    def pop_front(self):

        if self.hwm == self.lwm:
            return -1

        else:

            r = self.repo[self.lwm]

            self.lwm = self.lwm+1

            return r

    def pop_back(self):

        if self.hwm == self.lwm:
            return -1

        else:
            self.hwm = self.hwm-1

            r = self.repo[self.hwm]

            return r

    def size(self):
        return self.hwm - self.lwm

    def empty(self):
        return 1 if self.hwm == self.lwm else 0

    def front(self):

        if self.hwm == self.lwm:
            return -1

        else:
            return self.repo[self.lwm]

    def back(self):

        if self.hwm == self.lwm:
            return -1

        else:
            return self.repo[self.hwm - 1]

class Deque10866:
    
    deque = None

    def dequeProccess(self):

        size = int(read())

        self.deque = Deque(size) # 스택 사이즈를 최대 크기만큼 할당

        for loop in range(0, size):
     
            c = read().split() # 문자열로 \s를 사용하여 분리

            if util.isUnary(c): # 단항식일 경우 처리
                
                c = c[0] # 명령자(command allow)

                if c == 'pop': # pop command
                    print(self.deque.pop())
                elif c == 'pop_front': # pop_front command
                    print(self.deque.pop_front())
                elif c == 'pop_back': # pop_back command
                    print(self.deque.pop_back())
                elif c == 'empty': # empty command
                    print(self.deque.empty())
                elif c == 'front': # front command
                    print(self.deque.front())
                elif c == 'size': # size command
                    print(self.deque.size())
                elif c == 'back': # back command
                    print(self.deque.back())

            elif util.isBinary(c):
                
                c,r = c
                
                if c == 'push_back': # push_back command
                    self.deque.push_back(r)
                elif c == 'push_front': # push_front command
                    self.deque.push_front(r)

    def run(self):

        self.dequeProccess()

# test asseting
util.run([
    Deque10866()
])