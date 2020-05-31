import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1676 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine());
		int result = 0;

		for(int i=5; i<=n; i*=5) {
			result += n/i;
		}
		System.out.println(result);
	}
}
