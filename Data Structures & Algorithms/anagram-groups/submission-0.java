class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();

        Map<String, List<String>> hashToStr = new HashMap<>();
        for (int i=0; i<strs.length; i++) {
            char[] hash = strs[i].toCharArray();
            Arrays.sort(hash);
            String newHash = new String(hash);
            if (hashToStr.containsKey(newHash)) {
                hashToStr.get(newHash).add(strs[i]);
            } else {
                hashToStr.put(newHash, new ArrayList<String>(List.of(strs[i])));
            }
        }
        for (String key : hashToStr.keySet()) {
            result.add(hashToStr.get(key));
        }
        return result;

    }
}
