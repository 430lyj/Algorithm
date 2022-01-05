import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_1149 {
    final static int R = 0;
    final static int G = 1;
    final static int B = 2;
    public static int solution(int n, int[][] rgb){
        for (int i=1;i<n;i++){
            rgb[i][R] += Math.min(rgb[i-1][G], rgb[i-1][B]);
            rgb[i][G] += Math.min(rgb[i-1][R], rgb[i-1][B]);
            rgb[i][B] += Math.min(rgb[i-1][R], rgb[i-1][G]);
        }
        return Arrays.stream(rgb[n-1]).min().getAsInt();
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] rgb = new int [n][3];
        for (int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            rgb[i][R] = Integer.parseInt(st.nextToken());
            rgb[i][G] = Integer.parseInt(st.nextToken());
            rgb[i][B] = Integer.parseInt(st.nextToken());
        }
        int answer = solution(n, rgb);
        System.out.println(answer);
    }
}
