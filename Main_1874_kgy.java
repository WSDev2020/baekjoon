package baekjoon.algorithm.kgy;

import java.util.Scanner;
import java.util.Stack;

public class Main_1874_kgy {

	public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      Stack<Integer> stack = new Stack<Integer>();
      StringBuilder sb = new StringBuilder();
      int count = sc.nextInt();
      int[] array = new int[count];
      int idx = 0;
      
      //출력에 사용할 수열을 모음
      for(int i=0; i<count; i++) {
    	  array[i] = sc.nextInt();
      }
      
      for(int i=1; i<=count; i++) {
    	  //오름차순으로 1부터 스택에 수열을 넣음 
    	  stack.push(i);
    	  sb.append("+\n");
    	  //스택이 비워져 있지 않고 현재 수열의 값과 스택의 마지막 값이 같을 경우 pop 
    	  while(!stack.isEmpty() && array[idx] == (int)stack.peek()) {
    		  idx++;
    		  stack.pop();
    		  sb.append("-\n");
    	  }
      }
      
      //스택의 모든 값은 다 사용되어야 함 있을 경우 다 사용되지 않은 것 임으로 NO 출력
      if(!stack.isEmpty()) {
    	  System.out.println("NO");
      //스택의 모든 값을 다 사용했을 경우 정상적임으로 +- 결과를 출력	  
      }else {
    	  System.out.println(sb.toString());
      }
     
	}

}
