package baekjoon.algorithm.kgy;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main_1158_kgy {

   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int k = sc.nextInt();
      List<Integer> result = new ArrayList<Integer>();
      LinkedList<Integer> queue = new LinkedList<Integer>();
      for(int i=1; i<=n; i++){
         queue.offer(i);
      }
      int check = 1;
      while(queue.size() != 0){
         if(check == k){
            result.add(queue.poll());
            check = 1;
         }else{
            queue.offer(queue.poll());
            check++;
         }
      }
      System.out.println((result.toString().replace("[", "<")).replace("]", ">"));
   }

}
