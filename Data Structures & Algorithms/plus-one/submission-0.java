class Solution {
    public int[] plusOne(int[] digits) {
        boolean flag = false;
        digits[digits.length - 1] += 1;
        for (int i=digits.length - 1; i>=0; i--) {
            if (digits[i] >= 10) {
                digits[i] %= 10;
                if ( i == 0 ) {
                    flag = true;
                } else {
                    digits[i-1] += 1;
                }
            }
        }
        if (flag) {
            int[] arr = new int[digits.length + 1];
            for (int i=1; i<digits.length + 1; i++) {
                arr[i] = digits[i-1];
            }
            arr[0] = 1;
            return arr;
        } else {
            return digits;
        }
    }
}
