class Solution {
    public int numRescueBoats(int[] people, int limit) {
        //1 2 2 3 3
        //l       r 
        //boat = 1
        //l     r
        //boat = 2;
        //l   r 
        //boat = 3;
        //  
        int l = 0;
        int r = people.length-1;
        int boats = 0;
        if(people.length == 1){
            return 1;
        }
        Arrays.sort(people);
        while(l <= r){
            if(people[r] + people[l] > limit){
                boats++;
                r--;
            }else{
                boats++;
                l++;
                r--;
            }
        }
        return boats;
    }
}