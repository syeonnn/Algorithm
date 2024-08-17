class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        for (int i=0; i<=r2; i++) {
            double s = 0;
            
            if (i<r1) {
                s = Math.ceil(Math.sqrt(Math.pow(r1,2)-Math.pow(i,2)));
            }
            double e = Math.floor(Math.sqrt(Math.pow(r2,2)-Math.pow(i,2)));
            
            // 큰원에서의 y좌표 - 작은원에서의 y좌표
			answer += e - s + 1;
        }
        
        long minus = (r2 - r1 + 1) * 4;
        return answer * 4 - minus;
    }
}