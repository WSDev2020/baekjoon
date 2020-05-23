package baekjoon.algorithm.kgy;

import java.util.ArrayList;
import java.util.Scanner;

public class Main_6588_kgy {

   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      while(true){
        ArrayList<Integer> list = new ArrayList<Integer>();   
        int input = sc.nextInt();
        if(input == 0){
           break;
        }else{
           int count = input/2;
           for(int i=1; i<count+1; i++){
              int a = i;
              int b = input - a;
              if(check(a) && check(b)){
                list.add(a);
                list.add(b);  
              }
           }
           if(list.size() == 0){
             System.out.println("Goldbach's conjecture is wrong.");
           }else{
             int tmpA = 0; int tmpB = 0; int tmpC = 0; 
             for(int y=0; y<list.size()/2; y++){
                if(y==0){ 
                  tmpA = list.get(y*2);
                  tmpB = list.get((y*2)+1);
                  tmpC = tmpB - tmpA;
                }else{
                  if(tmpC < (list.get((y*2)+1) - list.get(y*2))){
                     tmpA = list.get(y*2);
                     tmpB = list.get((y*2)+1);
                     tmpC = tmpB - tmpA;
                  }
                }
             }
             System.out.println(input + " = "+tmpA+" + "+tmpB);
           }
        }
      
      }

   }

   public static boolean check(int num){
      boolean result = false;
      
      long tmp = 1;
      int check = 0;
      while(num >= tmp){
         if((num%tmp) == 0){
            check++;
         }
         tmp++;
      }
      if(check == 2){
           result = true;
      }
      
      return result;
   }
}
