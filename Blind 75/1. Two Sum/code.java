class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> num_location = new HashMap<>();

        for (int i = 0; i < nums.length; ++i) {
            int current_num = nums[i];
            int complement = target - current_num;

            if (num_location.containsKey(complement))
                return new int[] { num_location.get(complement), i };
            else
                num_location.put(current_num, i);
        }

        return new int[] {};
    }
}