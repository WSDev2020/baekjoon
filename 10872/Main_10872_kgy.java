package baekjoon.algorithm.kgy;

import java.util.Scanner;

public class Main_10872_kgy {

	 public static void main(String[] args) {
         
	        Scanner sc= new Scanner(System.in);
	        int number=sc.nextInt();
	        int tmp=1;
	         
	        for(int i=number;i>0;i--) {
	            tmp=tmp*i;
	             
	        }
	        System.out.println(tmp);
	  }
    
}