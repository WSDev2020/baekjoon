#! python3
# -*- coding: utf-8 -*- 
import sys # system module
import math as Math

###########################################
# 추가 된 부분
# Josephus1158
# BlackJeck2798
# Queue10845
###########################################

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
# 10828     스택
#
# basic time complexity = n(o)
###########################################
class Stack:

    # __init__ : <p>생성자</p>
    #     @param size:int 초기배열 사이즈
    #
    # push : <p>값을 배열의 끝 부분에 추가 하는 함수</p>
    #     @param e:object 등록 할 값
    #
    # pop : <p>배열의 마지막 값을 추출 하는 함수</p>
    #     @return r:str 배열의 마지막 값
    #
    # size : <p>배열의 사이즈(길이)를 반환하는 함수</p>
    #     @return r:int 배열의 길이
    #
    # empty : <p>배열이 비어 있을 경우 -1 비어 있지 않을 경우 1을 반환하는 함수</p>
    #     @return r:int 배열의 길이 검증값
    #
    # top : <p>현재 포지션이 배열의 마지막이면 1 그렇지 않으면 0을 반환하는 함수</p>
    #     @return r:int 배열이 마지막 여부

    r   = None # 메모리 저장소
    hwm = 0    # 최종 High Water Marking

    def __init__(self, *size):

        self.r = [0 for i in range(0 if len(size) == 0 else int(size[0]))]

    def push(self, e):

        self.r[self.hwm] = e
        self.hwm = self.hwm + 1

    def pop(self):

        if self.hwm == 0:
            return -1

        else:
            self.hwm = self.hwm - 1
            return self.r[self.hwm]
    
    def size(self):

        return self.hwm

    def empty(self):

        return 1 if self.hwm == 0 else 0

    def top(self):

        return -1 if self.hwm == 0 else self.r[self.hwm-1]

class Stack10828:

    # stackExecute : <p> 스택을 처리 하는 함수 </p>
    #     @return r:int 단항 연산자 여부
    #
    # run : <p> 알고리즘을 확인을 위한 테스트 </p>

    stack = None

    def stackProccess(self):

        size = int(read())

        self.stack = Stack(size) # 스택 사이즈를 최대 크기만큼 할당

        for loop in range(0, size):
     
            c = read().split() # 문자열로 \s를 사용하여 분리

            if util.isUnary(c): # 단항식일 경우 처리
                
                c = c[0] # 명령자(command allow)

                if c == 'pop': # pop command
                    print(self.stack.pop())
                elif c == 'size': # size command
                    print(self.stack.size())
                elif c == 'empty': # empty command
                    print(self.stack.empty())
                elif c == 'top': # top command
                    print(self.stack.top())

            elif util.isBinary(c):
                
                c,r = c
                
                if c == 'push': # push command
                    self.stack.push(r)

    def run(self):

        self.stackProccess()



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


###########################################
# no        title
# 9012      괄호
# 
# basic time complexity = o(n)
###########################################
class Bracket9012:

    # bracket : <p> 괄호의 VPS여부를 확인하는 함수 </p>
    #     @return w:str 확인할 문자열
    #
    # run : <p> 알고리즘을 확인을 위한 테스트 </p>

    def bracket(self, w):

        m = len(w)
        r = 0 # 검증을 위하여 초기화 포지션(0) 할당
        for i in range(m):

            c = w[i]

            if c == '(': # VPS 시작 지점
                r = r + 1
            elif c == ')': # VPS 종료 지정
                if r == 0: return 0 # VPS가 시작 전 종료 구문이 있을 경우 0처리
                r = r - 1
            else: continue

        return 1 if r == 0 else 0

    def run(self):

        size = int(read())

        for loop in range(size):
            print( 'YES' if self.bracket(read()[:-1]) == 1 else 'NO' )

###########################################
# no        title
# 1874      스택 수열
# 
# basic time complexity = o(n) * o(n * 2)
###########################################
class StackNumber1874:

    # listStack : <p> 리스트 팝업과 배열 검증을 위한 함수 </p>
    #     @return nl:array 확인할 수열
    #
    # run : <p> 알고리즘을 확인을 위한 테스트 </p>

    def listStack(self, nl):

        s = len(nl)
        l = [1 for i in range(s)] # 배열 검증을 위하여 수열과 같은 크기의 배열 선언 및 초기값(1) 할당
        n = [1 for i in range(s * 2)] # 리스트 팝업을 위하여 2(push, pop) * n 만큼의 크기의 배열 선언
        p = 0 # 배열 검증을 위한 포지션
        m = 0 # 리스트 팝업을 휘한 포지션

        for i in nl:

            if p > i: # 수열의 이전 수가 현재수 보다 클 경우

                for u in range(i, p-1): # 현재 포지션에서 이전 포지션을 순회 하며 수열 검증

                    if l[u] == 1: # [1, 1, 1(i), 1(u), 0(p)]일 경우 'NO'출력

                        return print('NO')

            else: # 현재수가 클 경우이므로 이전수에서 부터 현재 수까지 push(+) 처리

                for u in range(p, i):

                    if l[u] == 1: # [1, 1, 1, 0(p), 0(pass), 1(+), 1(+, i)] 처리 및 리스트 팝업 길이 증가

                        n[m] = '+'
                        m = m + 1

            n[m] = '-' # 현재 수를 찾았으니 pop(-)처리
            m = m + 1 # 리스트 팝업 길이 증가
            p = i # 이전 포지션 > 다음 포지션으로 이동
            l[p-1] = 0 # 포지션 처리를 종료 하였으므로 0 변환

        for u in n:
            print(u)

    def run(self):
        r = int(read())
        
        l = [int(read()) for v in range(r)]

        self.listStack(l)


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

###########################################
# no        title
# 1158      요세푸스
# 
# basic time complexity = o(n)
###########################################
class Josephus1158:

    repo = None
    rpof = []

    def josephus(self, k, n):

        ac = n
        ap = n

        self.repo = [v+1 for v in range(k)]

        while(len(self.repo) > 0): #배열 순환
            
            if ac == n: # n(x) 일 경우 배열 이동

                ap = ap - 1 # appointment를 한칸 아래로 이동(배열을 위한 인덱싱 처리)

                self.rpof.append(str(self.repo[ap])) # repository의 값을 repo forward로 이동

                del self.repo[ap] # respotiroy의 값 제거

            ac = 1 if ac == n else ac + 1 ## n값이 최대일 경우 처리
            ap = 1 if ap >= len(self.repo) else ap + 1 ## k값에 만날 경우 처리

        print("<{0}>".format(','.join(self.rpof)))

    def run(self):

        k, n = [int(v) for v in input().split()]
        self.josephus(k, n)

        
        
###########################################
# no        title
# 10872     팩토리얼
# 
# basic time complexity = o(n)
###########################################
class Factorial10872:

    def factorial(self, n):
        
        return n * self.factorial(n -1) if n > 1 else 1

    def run(self):

        print(self.factorial(int(input())))

class Fibonacci10870:
    def fibonacci(self, n):

        if n == 0: return print(0) # 0일 경우
        if n == 1: return print(1) # 1일 경우

        r = 0
        p = 1
        v = p

        for i in range(n-1):
            v = r + p
            r = p
            p = v

        print(p)

    def run(self):

        self.fibonacci(int(input()))


###########################################
# no        title
# 2557      Hello World!
###########################################
class HelloWorld2557:

    def run(self):
        print('Hello World!')

###########################################
# no        title
# 9653      스타워즈
###########################################
class Starwars9653:

    def starwars(self):

        print('    8888888888  888    88888')
        print('   88     88   88 88   88  88')
        print('    8888  88  88   88  88888')
        print('       88 88 888888888 88   88')
        print('88888888  88 88     88 88    888888')
        print('')
        print('88  88  88   888    88888    888888')
        print('88  88  88  88 88   88  88  88')
        print('88 8888 88 88   88  88888    8888')
        print(' 888  888 888888888 88  88      88')
        print('  88  88  88     88 88   88888888')

    def run(self):

        self.starwars()


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
    # Editor1406()
    # Josephus1158()
    # StackNumber1874()
    # HelloWorld2557()
     BlackJeck2798()
    # Bracket9012()
    # ReverseWord9093()
    # Starwars9653()
    # Stack10828()
    # Queue10845()
    # Fibonacci10870()
    # Factorial10872()
])
