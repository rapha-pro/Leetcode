class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagram_group = new HashMap<>();

        for (String s : strs) {
            int[] str_representation = new int[26];
            for (char c : s.toCharArray())
                str_representation[c - 'a']++;

            String key = Arrays.toString(str_representation);
            anagram_group.putIfAbsent(key, new ArrayList<>());
            anagram_group.get(key).add(s);
        }


        return new ArrayList<>(anagram_group.values());
    }
}
