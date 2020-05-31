import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

/**
 * 13588KB	84ms 	Java
 *
 */

public class Main_01676_jizero {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine());
        BigInteger result =factorial(n);
        String resStr = String.valueOf(result);
        String resStrRemove = resStr.replaceAll("0+$", "");
        System.out.println( resStr.length()-resStrRemove.length());
    }

    public static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        for(int i=1; i<=n; i++)
        result = result.multiply(BigInteger.valueOf(i));
        return result;
    }
}


