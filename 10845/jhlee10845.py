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
# 10845     큐
# 
# basic time complexity = o(n)
###########################################
class Queue:

    # __init__ : <p>생성자</p>
    #     @param size:int 초기배열 사이즈
    #
    # push : <p>값을 배열의 끝 부분에 추가 하는 함수</p>
    #     @param e:object 등록 할 값
    #
    # pop : <p>배열의 처음 값을 추출 하는 함수</p>
    #     @return r:str 배열의 마지막 값
    #
    # size : <p>배열의 사이즈(길이)를 반환하는 함수</p>
    #     @return r:int 배열의 길이
    #
    # empty : <p>배열이 비어 있을 경우 -1 비어 있지 않을 경우 1을 반환하는 함수</p>
    #     @return r:int 배열의 길이 검증 값
    #
    # front : <p>큐의 가장 앞에 있는 엘리먼트를 반환(엘리먼트 삭제 X)</p>
    #     @return r:int 배열의 가장앞에 있는 엘리먼트
    #
    # back : <p>큐의 가장 뒤에 있는 엘리먼트를 반환(엘리먼트 삭제 X)</p>
    #     @return r:int 배열의 가장뒤에 있는 엘리먼트

    repo = None
    hwm = 0
    lwm = 0
    
    def __init__(self, *size):
        self.repo = [0 for i in range(0 if len(size) == 0 else int(size[0]))]

    def push(self, e):
        self.repo[self.hwm] = e
        self.hwm = self.hwm+1

    def pop(self):

        if self.hwm == self.lwm:
            return -1

        else:

            r = self.repo[self.lwm]

            self.lwm = self.lwm+1

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

class Queue10845:

    queue = None

    def queueProccess(self):

        size = int(read())

        self.queue = Queue(size) # 스택 사이즈를 최대 크기만큼 할당

        for loop in range(0, size):
     
            c = read().split() # 문자열로 \s를 사용하여 분리

            if util.isUnary(c): # 단항식일 경우 처리
                
                c = c[0] # 명령자(command allow)

                if c == 'pop': # pop command
                    print(self.queue.pop())
                elif c == 'size': # size command
                    print(self.queue.size())
                elif c == 'empty': # empty command
                    print(self.queue.empty())
                elif c == 'front': # front command
                    print(self.queue.front())
                elif c == 'back': # back command
                    print(self.queue.back())

            elif util.isBinary(c):
                
                c,r = c
                
                if c == 'push': # push command
                    self.queue.push(r)

    def run(self):

        self.queueProccess()

# test asseting
util.run([
    Queue10845()
])