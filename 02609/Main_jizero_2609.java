import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 12912KB	68ms 	Java
 *
 */

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine()," ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int G = GCF(a, b);
        long L = a*b/G;
        System.out.println(G);
        System.out.println(L);
    }

    public static int GCF(int a, int b){
        if (b==0){
            return a;
        }else{
            return GCF(b, a%b);
        }
    }

}
