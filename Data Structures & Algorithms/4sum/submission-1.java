class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        //-1 -1 -1 1 1 1
        // i  x  l     r 
        //sum = -2 < 2
        //-1 -1 -1 1 1 1
        // i  x    l   r 
        //sum = 0 < 2
        //-1 -1 -1 1 1 1
        // i  x      l r 
        //sum = 0 < 2
        //-1 -1 -1 1 1 1
        // i     x l   r 
        //sum = 0 < 2
        //-1 -1 -1 1 1 1
        // i       x l r 
        //sum = 2 < 2
        if(nums.length < 4){
            return null;
        }
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList();
        int i = 0;
        int x = i + 1;
        int l = x + 1;
        int r = nums.length-1;
        while(i < nums.length-3){
            while(x < nums.length-2){
                while(l < r){
                    long sum = nums[i];
                    sum = sum + nums[x];
                    sum = sum + nums[l];
                    sum = sum + nums[r];
                    System.out.println("sum: " + sum);
                    if(sum < target){
                        l++;
                    }else if(sum > target){
                        r--;
                    }else{
                        List<Integer> quad = new ArrayList();
                        quad.add(nums[i]);
                        quad.add(nums[x]);
                        quad.add(nums[l]);
                        quad.add(nums[r]);
                        ans.add(quad);
                        l++;
                        while(l < r && nums[l] == nums[l-1]){
                            l++;
                        }
                    }
                }
                x++;
                while(x < nums.length-2 && nums[x] == nums[x-1]){
                    x++;
                }
                l = x + 1;
                r = nums.length-1;
            }
            i++;
            while(i < nums.length-3 && nums[i] == nums[i-1]){
                i++;
            }
            x = i + 1;
            l = x + 1;
            r = nums.length-1;
        }
        return ans;

    }
}