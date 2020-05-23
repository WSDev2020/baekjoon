package baekjoon.algorithm.kgy;

import java.util.Scanner;

public class Main_2609_kgy {

   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      long n1 = sc.nextLong();
      long n2 = sc.nextLong();
      
      long gcd = getGCF(Math.max(n1, n2), Math.min(n1, n2));
      long lcm = getLCM(n1, n2, gcd);
      System.out.println(gcd);
        System.out.println(lcm);
   }

   //최대 공약수 Greatest common factor
   //유클리드 호제 법 : 큰 수 A를 작은 수 B로 나누었을 때 나누어 떨어지면 최대공약수는 B가 된다.
   public static long getGCF(long a, long b){
      while(b > 0) {
         long tmp = a;
         a = b;
         b = tmp%b;
      }
      return a;
   }
   
   //최소 공배수 Least common multiple
   //두수를 곱하고 최대 공약수로 나누면 최소 공배수가 나온다.
   public static long getLCM(long a, long b, long gcd){
      return (a*b)/gcd;
   }
}
