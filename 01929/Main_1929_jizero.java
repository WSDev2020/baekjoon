import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 37388KB	580ms 	Java
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
                BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");


        int n = Integer.parseInt(st.nextToken());//n
        int m = Integer.parseInt(st.nextToken());
        boolean[] s = new boolean[m+1];
        s[0] = true;
        s[1] = true;
        for (int i = 2; i*i <= m; i++) {
            if (s[i] == false) {
                for (int j = i*i; j <= m; j += i) {
                    s[j] = true;
                }
            }
        }

        for(int i=n; i<=m; i++) {
            if(false == s[i]) {
                System.out.println(i);
            }
        }

    }

}
