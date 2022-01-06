import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;
class location{
    int i;int j;
    public int getI() {
        return i;
    }
    public int getJ() {
        return j;
    }
    location (int i, int j){
        this.i = i;
        this.j = j;
    }
}

public class baekjoon_2178 {
    public static int solution(int n, int m, int[][] miro){
        Queue<location> queue = new LinkedList<>();
        int i = 0; int j = 0;
        while (i != n-1 || j != m-1){
            if (i< n-1){
                if (miro[i+1][j] == 1){
                    miro[i+1][j] += miro[i][j];
                    queue.add(new location(i+1, j));
                }
            }
            if (j < m-1){
                if (miro[i][j+1] == 1){
                    miro[i][j+1] += miro[i][j];
                    queue.add(new location(i, j+1));
                }
            }
            if (i > 0 ){
                if (miro[i-1][j] == 1){
                    miro[i-1][j] += miro[i][j];
                    queue.add(new location(i-1, j));
                }
            }
            if (j > 0){
                if (miro[i][j-1] == 1){
                    miro[i][j-1] += miro[i][j-1];
                    queue.add(new location(i, j-1));
                }
            }
            location temp = queue.poll();
            i = temp.getI();
            j = temp.getJ();
        }
        return miro[n-1][m-1];
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] miro = new int [n][m];
        for (int i=0;i<n;i++){
            String string = br.readLine();
            char[] ch = string.toCharArray();
            for (int j=0;j<m;j++) {
                miro[i][j] = Character.getNumericValue(ch[j]);
            }
        }
        int answer = solution(n, m, miro);
        System.out.println(answer);
    }
}
