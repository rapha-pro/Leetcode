import java.util.ArrayList;

class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> fizzBuzz_array = new ArrayList();

        for(int i = 1; i <= n; ++i) {

            String isFizzBuzz = "";
            boolean divisibleBy3 = i%3 == 0;
            boolean divisibleBy5 = i%5 == 0;

            if(divisibleBy3) {
                isFizzBuzz += "Fizz";
            }
            if(divisibleBy5) {
                isFizzBuzz += "Buzz";
            } else if (!(divisibleBy3 || divisibleBy5)) {
                isFizzBuzz += i;      // or use String.valueOf(i)
            }
            fizzBuzz_array.add(isFizzBuzz);

        }

        return fizzBuzz_array;
    }
}