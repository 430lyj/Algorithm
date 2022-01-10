import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_1789 {
    public static long solution(long n){
        long total = 0;
        long count = 0;
        while (total < n){
            total = total + count;
            count++;
        }
        if (total > n) return (count - 2);
        return (count - 1);
    }
    public static void main(String args[]) throws  IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());
        long answer = solution(n);
        System.out.println(answer);
    }
}