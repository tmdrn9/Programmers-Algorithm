import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int front,cnt;
        Queue<Integer>queue=new LinkedList<Integer>();
        LinkedList<Integer>list=new LinkedList<Integer>();
        
        for(int i=0;i<progresses.length;i++){
            queue.add((int)Math.ceil((double)(100-progresses[i])/(double)speeds[i]));
        }
        
        while(!queue.isEmpty()){
            cnt=1;
            front=queue.remove();
            while(!queue.isEmpty()&&front>=queue.peek()){
                queue.remove();
                cnt++;
            }   
            list.add(cnt);
        }

        int[] answer = new int[list.size()];
        
        Iterator<Integer> iter = list.iterator(); //Iterator 선언 
        for(int i=0;i<list.size();i++){
            answer[i]=iter.next();
        }
       
        return answer;
    }
}