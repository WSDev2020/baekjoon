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
# 9093      단어 뒤집기
#
# basic time complexity = w * log(n)
###########################################
class ReverseWord9093:

    # reverse : <p> 단어를 거꾸로 변환하는 함수 </p>
    #     @return r:int 단항 연산자 여부
    #
    # run : <p> 알고리즘을 확인을 위한 테스트 </p>

    def reverse(self, word): # n(o) = logN = n(o) / 2
        l = len(word) # 단어의 길이를 확인하기 위하여 전체 길이 할당

        h = Math.ceil(l/2) # 단어의 중간 포지션을 사용하여 단어 스와핑을 적용하기 위하여 할당

        s = ['' for v in range(l)] # 초기화 및 최초 값 할당

        for i in range(h): # 단어를 순환하면서 스와핑 처리
            s[l - i - 1] = word[i]
            s[i] = word[l - i - 1]

        return ''.join(s)

    def run(self):

        size = int(read())

        for loop in range(0, size):

            str = input().split() 

            new_word = ''

            for sp_str in str: # w = 3
                new_word = new_word + self.reverse(sp_str) + ' '

            print(new_word[:-1])

# test asseting
util.run([
    ReverseWord9093()
])