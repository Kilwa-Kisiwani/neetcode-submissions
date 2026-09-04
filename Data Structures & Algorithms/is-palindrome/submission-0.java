class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().trim().replaceAll("[^a-zA-Z0-9]", "");
        int len = s.length();
        int i = 0;
        int j = len - 1;
        while (i < j) {
            if (s.charAt(i)!=s.charAt(j)) {
                System.out.println(s.charAt(i) + " != " + s.charAt(j));
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
