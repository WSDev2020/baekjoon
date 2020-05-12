import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class Problem1158 {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        LinkedList<Integer> list = new LinkedList<Integer>();
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());//n
        int m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            list.add(i);
        }
        int idx = m-1;

        StringBuilder result = new StringBuilder("<");

        while (list.size() > 1) {

            System.out.println("====="+list.size());
            result.append(list.get(idx)+ ", ");
            list.remove(idx);

            idx += m - 1;
            System.out.println(list);
            System.out.println(result);

              idx %= list.size();

        }

        result.append(list.getLast()+">");
        System.out.println(result);
    }
}

