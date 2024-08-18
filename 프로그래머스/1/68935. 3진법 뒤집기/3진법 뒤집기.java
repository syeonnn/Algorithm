import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        ArrayList<Integer> arrBy3 = new ArrayList<>();
        int nBy3 = 0;

        while(n >= 3){
            arrBy3.add(n % 3);
            n /= 3;
        }
        arrBy3.add(n);
        
        Collections.reverse(arrBy3);
        
        for (int i = 0; i < arrBy3.size(); i++) {
            answer += arrBy3.get(i) * Math.pow(3,i);
        }

        return answer;
    }
}