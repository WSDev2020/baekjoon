import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main_10845 {
	
	static Queue<Integer> queue = new LinkedList<Integer>();
	static ArrayList<Integer> list = new ArrayList<Integer>();
	static int rear = -1;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = Integer.parseInt(sc.nextLine());
//		Data data = new  Data();
		String command = "";
		for(int i=0; i<n; i++) {
			command = sc.nextLine();
			if(command.contains("push")) {
				dataPush(Integer.parseInt(command.replace("push ", "")));
			} else if(command.equals("pop")) {
				dataPop();
			} else if(command.equals("size")) {
				size();
			} else  if(command.equals("empty")) {
				empty();
			} else if(command.equals("front")) {
				front();
			} else if(command.equals("back")) {
				back();
			}
		}
	}
	
	public static void back() {
		System.out.println((queue.size() == 0) ? "-1" : list.get(rear));
	}

	public static void front() {
		System.out.println((queue.size() == 0) ? "-1": queue.peek());
	}

	public static void empty() {
		System.out.println((queue.size() == 0) ? "1" : "0");
	}

	public static void size() {
		System.out.println(queue.size());
	}

	public static void dataPop() {
		System.out.println(queue.size() == 0 ? "-1" : queue.poll());
	}

	public static void dataPush(int data) {
		queue.offer(data);
		list.add(data);
		rear++;
	}

}