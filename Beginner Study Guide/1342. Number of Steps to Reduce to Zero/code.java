class Solution {
    public int numberOfSteps(int num) {
        int numOfSteps = 0;

        while(num > 0) {
            boolean isEven = (num & 1) == 0;
            num = isEven ? num >>= 1 : num ^ 1;
            numOfSteps++;
        }

        return numOfSteps;
    }
}