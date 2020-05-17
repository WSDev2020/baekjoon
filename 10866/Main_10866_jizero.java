import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 19716KB	288ms 	Java
 *
 */

public class  Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());

        LinkedList<Integer> list = new LinkedList<>();

        for(int i=0; i<N; i++){
            String[] CMD = in.readLine().split(" ");
            if(CMD[0].equals("push_front")){
                list.addFirst(Integer.parseInt(CMD[1]));
            }else if(CMD[0].equals("push_back")){
                list.addLast(Integer.parseInt(CMD[1]));
            }else if(CMD[0].equals("pop_front")){
                System.out.println(list.isEmpty() ? -1 : list.pollFirst());
            }else if(CMD[0].equals("pop_back")){
                System.out.println(list.isEmpty() ? -1 : list.pollLast());
            }else if(CMD[0].equals("size")){
                System.out.println(list.size());
            }else if(CMD[0].equals("empty")){
                System.out.println(list.isEmpty() ? 1 : 0);
            }else if(CMD[0].equals("front")){
                //front: 덱의 가장 앞에 있는 정수를 출력한다.
                System.out.println(list.isEmpty() ? -1 : list.peekFirst());
            }else if(CMD[0].equals("back")) {
                //back: 덱의 가장 뒤에 있는 정수를 출력한다
                System.out.println(list.isEmpty() ? -1 : list.peekLast());
            }else{
                System.out.println("error");
            }
        }

    }

}
