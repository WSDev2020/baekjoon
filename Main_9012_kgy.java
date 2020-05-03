package baekjoon.algorithm.kgy;

import java.util.Scanner;

public class Main_9012_kgy {

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
	    	while(true) {
	    		String tmp = sc.nextLine();
	    		if(tmp.length() >= 2 && tmp.length() <= 50) {
			    	char[] chars = tmp.toCharArray();
			    	int check = 0;
			    	String result = "YES";
			    	for(int y=0 ; y < chars.length; y++) {
			    		if(chars[y] == '(') {
			    			check++;
			    		}
			    		if(chars[y] == ')') {
			    			check--;
			    		}
			    		if(check < 0) {
			    			result = "NO";
			    			break;
			    		}
			    	}
			    	if(check != 0) {
			    		result = "NO";
			    	}
			    	System.out.println(result);
			    	break;
			   }
	    	}
	      }	
	}

}
