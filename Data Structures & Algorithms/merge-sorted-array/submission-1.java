class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[nums1.length];
        int l = 0;
        int r = 0;
        int i = 0;
        while(l < m && r < n){
            if(nums1[l] <= nums2[r]){
                temp[i] = nums1[l];
                i++;
                l++;
            }else if(nums1[l] > nums2[r]){
                temp[i] = nums2[r];
                i++;
                r++;
            }
        }
        while(l < m){
            temp[i] = nums1[l];
            i++;
            l++;
        }
        while(r < n){
            temp[i] = nums2[r];
            i++;
            r++;
        }
        for(int x = 0; x < nums1.length; x++){
            nums1[x] = temp[x];
        }
    }
}