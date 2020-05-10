package baekjoon.algorithm.kgy;

import java.util.Scanner;
import java.util.Stack;

public class Main_1406_kgy {

	public static void main(String[] args) {
	  
	   Scanner sc = new Scanner(System.in);
	   String text = sc.next();
	   char[] chs = text.toCharArray();
	   Stack<Character> stackL = new Stack<Character>();
	   Stack<Character> stackR = new Stack<Character>();
	   for(int i=0; i<chs.length; i++) {
		   stackL.push(chs[i]);
	   }
	   int count = sc.nextInt();
	   for(int i=0; i < count; i++){
		  String command = sc.next();
		  if(command.equals("L")) {
			  if(stackL.size() != 0) {
				  stackR.push(stackL.pop());
			  }
		  }else if(command.equals("D")) {
			 if(stackR.size() != 0) {
				 stackL.push(stackR.pop());
			 }
		  }else if(command.equals("B")) {
			 if(stackL.size() != 0) {
			     stackL.pop();	  
			 }
		  }else if(command.equals("P")) {
			 char addText = sc.next().charAt(0);
			 stackL.push(addText); 
		  }
	   }
	   
	  /** String tmpL = "";
	   String tmpR = "";
	   if(stackL.size() > 0) {
		  int countL = stackL.size();
		  for(int i=0; i<countL; i++) {
			  tmpL = stackL.pop()+tmpL;
		  }
	   }
	   if(stackR.size() > 0) {
		   int countR = stackR.size();
		   for(int i=0; i<countR; i++) {
			   tmpR = tmpR+stackR.pop();
		   }
	   }**/
	   while(stackL.size() != 0) {
		   stackR.push(stackL.pop());
	   }
	   //System.out.println(tmpL+tmpR);
	   StringBuilder sb = new StringBuilder();
	   while(stackR.size() != 0) {
		   sb.append(stackR.pop());
	   }
	   System.out.println(sb.toString());
    }
}
