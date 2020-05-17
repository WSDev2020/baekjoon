import java.util.Scanner;

/*
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/

public class Main_10828_nhw {
	
	static String[] stack;
	static int top = -1;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		stack = new String[n]; 
		// sc.nextInt(); 바로 아래 sc.nextLine()사용시 스페이스바를 입력한것으로 반영되므로 더미를 둔다
		sc.nextLine();
		
		for(int i=0; i<n; i++) {
			String data = sc.nextLine();
			if(data.contains("push")) {
				push(data);
			} else if(data.equals("pop")) {
				pop(data);
			} else if(data.equals("size")) {
				size();
			} else if(data.equals("empty")) {
				empty();
			} else if(data.equals("top")) {
				top();
			} 
		}
	}

	private static void top() {
		if(top == -1) {
			System.out.println("-1");
		} else {
			System.out.println(stack[top].replace(" ", ""));
		}
	}
	private static void empty() {
		if(top == -1) {
			System.out.println("1");
		} else {
			System.out.println("0");
		}
	}
	private static void size() {
		System.out.println(top+1);
	}
	private static void pop(String data) {
		if(top != -1) {
			System.out.println(stack[top].replace(" ", ""));
			stack[top] = "";
			top -= 1;
		} else {
			System.out.println("-1");
		}
		
	}
	private static void push(String data) {
		// 명령과 아규먼트를 분리 
		top += 1;
		stack[top] = data.replace("push", "");
	}
}
