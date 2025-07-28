class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> uniques = new HashSet<Integer>();

        for (int n: nums) {
            if (uniques.contains(n)) return true;
            uniques.add(n);
        }

        return false;
    }
}