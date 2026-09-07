class Solution {
    public int maxArea(int[] heights) {
        int i = 0;
        int j = heights.length - 1;
        int curr = 0;
        while (i < j) {
            if (Math.min(heights[i], heights[j]) * (j - i) > curr) {
                curr = Math.min(heights[i], heights[j]) * (j - i);
            }
            if (heights[i] > heights[j]) {
                j--;
            } else {
                i++;
            }
        }
        return curr;

    }
}
