package baekjoon.algorithm.kgy;

import java.util.Scanner;

public class Main_9093_kgy {

	public static void main(String[] args) {
		int count = 0;
		
		Scanner sc = new Scanner(System.in);
		while(true){
	      if(sc.hasNextInt()){
	        count = sc.nextInt();
	        break;
	      }
	    }
		sc.nextLine(); 
		//입력받은 명령의 개수만큼 반복
	    for(int i=0; i < count; i++){
	      loop:
	      while(true) {
	       int check = 0;
	       String tmp = "";
	       String text = sc.nextLine(); 
	       String[] array = text.split(" ");
	       if(text.length() <= 1000) {
	    	   for(int y=0; y < array.length; y++) {
	  	    	 if(y==0) {
	    		  tmp = reverseString(array[y]);
	  	    	 }else {
	  	          tmp = tmp +" "+reverseString(array[y]);
	  	    	 }
	    		 if(array[y].length() > 20) {
	  		       check++;
	  		       break;
	  		     }
	  		   }
	    	   if(check == 0) {
	    		   System.out.println(tmp.toString());
	    		   break loop;
	    	   }
	       }	      
	      }
	       
	    }
	    sc.close();
	}
	
	 public static String reverseString(String s) {
		 return ( new StringBuffer(s) ).reverse().toString();
     }

}
