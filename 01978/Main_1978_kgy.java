package baekjoon.algorithm.kgy;

import java.util.Scanner;

public class Main_1978_kgy {

   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int count = sc.nextInt();
      int result = 0;
      for(int i=0; i<count; i++){
         long num = sc.nextLong();
         long tmp = 1;
         //소수란 약수가 자기 자신과 1로만 나눠지는 것
         int check = 0;
         while(num >= tmp){
            if((num%tmp) == 0){
               check++;
            }
            tmp++;
         }
         if(check == 2){
              result++;
         }
      }
      System.out.println(result);
   }

}
