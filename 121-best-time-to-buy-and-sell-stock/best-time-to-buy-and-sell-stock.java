class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buy = prices[0]; 

        for (int i =1; i< prices.length; i++){
            int profit = prices[i] - buy; 

            if(profit > maxProfit){
                maxProfit = profit;
            }

            if (prices[i] < buy){
                buy = prices[i];
            }
        }

        return maxProfit;
    }
}