class Solution {
    public int maxSubArray(int[] nums) {
        int curSum = nums[0];
        int maxSum = nums[0];

        for(int i=1; i< nums.length; i++){
            if(curSum + nums[i] <= 0 ){
                curSum = nums[i];
            }else{
                if(curSum<0){
                    curSum = nums[i];
                }else{
                    curSum += nums[i];
                }
            }
            
            if(curSum > maxSum){
                maxSum = curSum;
            }
        }
        
        return maxSum;
    }
}