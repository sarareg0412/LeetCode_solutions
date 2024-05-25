class Solution {
    public int search(int[] nums, int target) {
        int high = nums.length -1;
        int low = 0;
        int mid = 0;

        while (low <= high){
            mid = (high + low)/2;

            if(target == nums[mid]){
                return mid;
            }else{
                if(target < nums[mid]){
                    high = mid -1;
                }else{
                    low = mid + 1;
                }
            }
        }

        return -1;
    }
}