import java.util.Scanner;

/*
6							
(())())					NO
(((()())()				NO
(()())((()))			YES
((()()(()))(((())))()	NO
()()()()(()()())()		YES
(()((())()(				NO
*/

public class Main_9012_nhw {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		
		for(int i=0; i<n; i++) {
			int chk = 0;
			String str = sc.nextLine();
			String[] word = str.split("");

			for(int j=0; j<str.length(); j++) {
				if(word[j].equals("(")) {
					chk++;
				} else if(word[j].equals(")")) {
					chk--;
					if(chk<0) {
						break;
					}
				}
				
			}
			if(chk == 0) {
				System.out.println("YES");
			} else if(chk != 0) {
				System.out.println("NO");
			} 
		}
	}
}
