package baekjoon.algorithm.kgy;

import java.util.Scanner;
import java.util.Stack;

public class Main_10828_kgy {
   
   public static void main(String[] args) {
      int count = 0;
      Stack<Integer>  stack = new Stack<Integer>();
      //정수가 아니거나 범위가 1 ≤ N ≤ 10,000가 아닐 경우 입력을 계속 받음
      Scanner sc = new Scanner(System.in);
      while(true){
         if(sc.hasNextInt()){
           count = sc.nextInt();
           if(1 <= count && count <= 10000){
              break;
           }
         }
      }
      //입력받은 명령의 개수만큼 반복
      for(int i=0; i < count; i++){
         while(true){
          String command = sc.next();
          //명령어를  push를 입력한 경우
          if(command.equals("push")){
            try{
             int num = sc.nextInt();
             if(num < 1 || num > 100000){
                System.out.println("1보다 크거나 같고 100,000보다 작거나 같은 정수를 입력하세요.");
             }else{
                stack.push(num);
                break;
             }
            }catch(Exception e1){
                System.out.println("'명령어+띄어쓰기+정수' 형식으로 입력하세요.");
            }
          //명령어를 pop을 입력한 경우   
          }else if(command.equals("pop")){
            if(stack.size() == 0){
                System.out.println(-1);
            }else{
                System.out.println(stack.pop());
            }
            break;
          //명령어를 size를 입력한 경우   
          }else if(command.equals("size")){
            System.out.println(stack.size());
            break;
          //명령어를 empty를 입력한 경우   
          }else if(command.equals("empty")){
            if(stack.empty()){
               System.out.println(1);
            }else{
               System.out.println(0);
            }
            break;
          //명령어를 top을 입력한 경우   
          }else if(command.equals("top")){
            if(stack.size() == 0){
                System.out.println(-1);
            }else{
                System.out.println(stack.peek());
            }
            break;
          }
         }
      }
      sc.close();
   }
   
}