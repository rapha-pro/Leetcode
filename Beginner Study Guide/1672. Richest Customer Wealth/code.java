class Solution {
    public int runningSum(int[] nums) {
        int arrLength = nums.length;
        for(int i=1; i < arrLength; i++) {
            nums[i] += nums[i-1];
        }
        return nums[arrLength-1];
    }

    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;
        for(int i=0; i < accounts.length; ++i) {
            int currentCustomerWealth = runningSum(accounts[i]);
            maxWealth = Math.max(maxWealth, currentCustomerWealth);
        }
        return maxWealth;
    }
}