class Solution {
    HashMap<Character, Integer> map = new HashMap<>();
    HashMap<Character, Integer> map2 = new HashMap<>();
    public boolean isAnagram(String s, String t) {
            if (s.length() != t.length()) {
                return false;
            }

            char[] sArray = s.toCharArray();
            char[] tArray = t.toCharArray();
            for (int i = 0; i < sArray.length; i++) {
                map.put(sArray[i], map.getOrDefault(sArray[i], 0) + 1);
            }

            for (int i = 0; i < tArray.length; i++) {
                map2.put(tArray[i], map2.getOrDefault(tArray[i], 0) + 1);
            }

            return map.equals(map2);
    }
}
