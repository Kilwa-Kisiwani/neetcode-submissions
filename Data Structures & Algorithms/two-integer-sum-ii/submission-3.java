class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        while (l < r) {
            // if (numbers[l] > target) {
            //     // System.out.println(l + " : " + numbers[l]);
            //     return null;
            // }
            // else if (numbers[r] < target) {
            //     System.out.println(r + " : " + numbers[r]);
            //     return null;
            // }
            // else {
                if (target - numbers[l] == numbers[r]) {
                    return new int[]{l+1, r+1};
                }
                else if (target - numbers[l] < numbers[r]) {
                    // System.out.println("r = " + r + "--");
                    r--;
                }
                else {
                    // System.out.println("l = " + l + "++");
                    l++;
                }
            // }
        }
        // System.out.println("none");
        return null;
    }
}
