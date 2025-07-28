import java.util.HashMap;


class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
    
        if (magazine.length() < ransomNote.length()) return false;

        HashMap<Character, Integer> letter_freq = new HashMap<>();
        for(char c : magazine.toCharArray()) letter_freq.put(c, letter_freq.getOrDefault(c, 0) + 1);
        
        for(char c : ransomNote.toCharArray()){
            if(!letter_freq.containsKey(c) || letter_freq.get(c) < 1) return false;
            letter_freq.put(c, letter_freq.get(c) - 1);
        }
        
        return true;
    }
}


// see alternative solution link for explanation
class Solution2 {
    public boolean canConstruct(String ransomNote, String magazine) {
		if (ransomNote.length() > magazine.length()) return false;
        int[] alphabets_counter = new int[26];

        for (char c : magazine.toCharArray())
            alphabets_counter[c-'a']++;

        for (char c : ransomNote.toCharArray()){
            if (alphabets_counter[c-'a'] == 0) return false;
            alphabets_counter[c-'a']--;
        }
        return true;
    }
}