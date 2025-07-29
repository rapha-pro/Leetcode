class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] alphabet_counter = new int[26];

        for (char c : s.toCharArray())
            alphabet_counter[c-'a']++;

        for (char c: t.toCharArray()){
            if(alphabet_counter[c-'a'] == 0) return false;
            alphabet_counter[c-'a']--;
        }

        return true;
    }
}