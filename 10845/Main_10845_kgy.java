package baekjoon.algorithm.kgy;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class Main_10845_kgy {

   public static void main(String[] args) {
      LinkedList<Integer> queue = new LinkedList<Integer>();
      Scanner sc = new Scanner(System.in);
      int count = sc.nextInt();
      StringBuilder sb = new StringBuilder();
      
      for(int i=0; i<count; i++){
        String command = sc.next();
        if(command.equals("push")){
           int num = sc.nextInt();
           queue.offer(num);
        }else if(command.equals("pop")){
           if(queue.size() > 0){
              sb.append(queue.poll()+"\n");
           }else{
              sb.append(-1+"\n");
           }
        }else if(command.equals("size")){
           sb.append(queue.size()+"\n");
        }else if(command.equals("empty")){
           if(queue.size() == 0){
              sb.append(1+"\n");
           }else{
              sb.append(0+"\n");
           }
        }else if(command.equals("front")){
           if(queue.size() == 0){
              sb.append(-1+"\n");
           }else{
              sb.append(queue.peek()+"\n");
           }
        }else if(command.equals("back")){
           if(queue.size() == 0){
              sb.append(-1+"\n");
           }else{
              Collections.reverse(queue);
              sb.append(queue.peek()+"\n");
              Collections.reverse(queue);
           }
        }
      }
      
      System.out.println(sb.toString());
   }
}
