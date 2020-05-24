import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

/**
 * 30144 544 	Java
 *
 */

public class Main {

    //public static final int MAX = 200;
    public static final int MAX = 1000000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n;
        boolean[] s = new boolean[MAX];
        // 0과 1 제외
        s[0] = true;
        s[1] = true;
//        System.out.print(s[2]);
        for (int i = 2; i*i < MAX; i++) {
            if (s[i] == false) {
                for (int j = i*i; j < MAX; j += i) {
                    s[j] = true;
                }
            }
        }

/*
        for(int i=0; i<MAX; i+=1) {
            if(false == s[i]) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
*/

        while ((n = Integer.parseInt(br.readLine())) != 0) {
            if(n == 0) break;
            boolean gold = false;
            for(int i = 2; i <= n; i++) {
                if(!s[i] && !s[n-i]) {
                    System.out.println(n + " = " + i + " + " + (n-i));
                    gold = true;
                    break;
                }
            }
            if(!gold) System.out.println("Goldbach's conjecture is wrong.");
        }


    }

}
