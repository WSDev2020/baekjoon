package baekjoon.algorithm.kgy;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main_10866_kgy {

   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      StringBuilder sb = new StringBuilder();
      Deque<Integer> deque = new ArrayDeque<Integer>();
      
      for(int i=0; i<n; i++){
         String command = sc.next();
         if(command.equals("push_back")){
            int num = sc.nextInt();
            deque.offerLast(num);
         }else if(command.equals("push_front")){
            int num = sc.nextInt();
            deque.offerFirst(num);
         }else if(command.equals("pop_front")){
            if(deque.size() > 0){
               sb.append(deque.pollFirst()+"\n");   
            }else{
               sb.append(-1+"\n");
            }
         }else if(command.equals("pop_back")){
            if(deque.size() > 0){
               sb.append(deque.pollLast()+"\n");   
            }else{
               sb.append(-1+"\n");
            }
         }else if(command.equals("size")){
            sb.append(deque.size()+"\n");
         }else if(command.equals("empty")){
            if(deque.size() == 0){
                 sb.append(1+"\n");
             }else{
                 sb.append(0+"\n");
             }
         }else if(command.equals("front")){
            if(deque.size() > 0){
                 sb.append(deque.peekFirst()+"\n");
            }else{
                sb.append(-1+"\n");
            }
         }else if(command.equals("back")){
            if(deque.size() > 0){
                 sb.append(deque.peekLast()+"\n");
            }else{
                sb.append(-1+"\n");
            }     
         }
      }
      
      System.out.println(sb.toString());
   }

}
