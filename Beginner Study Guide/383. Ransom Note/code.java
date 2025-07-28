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

