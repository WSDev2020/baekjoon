package baekjoon.algorithm.kgy;

import java.util.Scanner;

public class Main_1676_kgy {

	public static void main(String[] args) {
		// 팩토리얼에서 0의 갯수를 찾으려면 5가 몇번 나오는지만 확인하면 된다.
		Scanner sc= new Scanner(System.in);
		int number=sc.nextInt();
		int cnt = 0;
		for( int i = 5; i<= number; i*=5) {    
			cnt += 	number/i;
        }
        System.out.println(cnt);
	}

}
