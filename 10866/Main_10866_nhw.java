import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main_10866_nhw {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Deque<String> deque = new LinkedList<String>();
		
		int n = Integer.parseInt(sc.nextLine());
		String command = "";
		for(int i=0; i<n; i++) {
			command = sc.nextLine();
			if(command.contains("push_front")) {
				deque.offerFirst(command.replace("push_front ", ""));
			} else if(command.contains("push_back")) {
				deque.offerLast(command.replace("push_back ", ""));
			} else if(command.equals("pop_front")) {
				System.out.println(deque.size() == 0 ? -1 : deque.pollFirst());
			} else if(command.equals("pop_back")) {
				System.out.println(deque.size() == 0 ? -1 : deque.pollLast());
			} else if(command.equals("size")) {
				System.out.println(deque.size());
			} else if(command.equals("empty")) {
				System.out.println(deque.size() == 0 ? 1 : 0);
			} else if(command.equals("front")) {
				System.out.println(deque.size() == 0 ? -1 : deque.peek());
			} else if(command.equals("back")) {
				System.out.println(deque.size() == 0 ? -1 : deque.peekLast());
			}
		}
	}
}

/*
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.


15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

2
1
2
0
2
1
-1
0
1
-1
0
3


*/