class Solution {
    public int numberOfSteps(int num) {
        int numOfSteps = 0;

        while(num > 0) {
            boolean isEven = (num & 1) == 0;

            if(isEven) {
                num >>= 1;
            } else {
                num--;
            }
            numOfSteps++;
        }

        return numOfSteps;

    }
}