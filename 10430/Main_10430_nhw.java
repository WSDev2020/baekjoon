import java.util.Scanner;

public class Main_10430_nhw {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		int aa = (a+b)%c;
		int bb = ((a%c)+(b%c))%c;
		int cc = (a*b)%c;
		int dd = ((a%c)*(b%c))%c;
		
		System.out.println(aa+"\n"+bb+"\n"+cc+"\n"+dd);
		
	}
}
