import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_1002 {
    public static int solution(int[] input){
        double distance = Math.sqrt(Math.pow((input[0] - input[3]), 2) + Math.pow((input[1] - input[4]), 2));
        int r1 = input[2]; int r2 = input[5];
        int r_max = r1 + r2;
        int r_min = Math.abs(r1 - r2);
        if (distance==0){
            if (r1 == r2) return -1;
            else return 0;
        }
        else{
            if (distance == r_max || distance == r_min) return 1;
            else if (distance < r_max && distance > r_min) return 2;
            else return 0;
        }
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] input = new int [6];
        int[] answer = new int[n];
        for (int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j=0; j<6;j++) {
                input[j] = Integer.parseInt(st.nextToken());
            }
            answer[i] = solution(input);
        }
        for (int i=0;i<n;i++){
            System.out.println(answer[i]);
        }
    }
}
