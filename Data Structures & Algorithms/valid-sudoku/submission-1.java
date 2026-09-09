class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i=0; i<board.length; i++) {
            Set<Character> presentInts = new HashSet<>();
            for (int j=0; j<board[0].length; j++) {
                if (board[i][j]>='1' && board[i][j] <= '9' && !presentInts.add(board[i][j])) {
                    System.out.println("False on stage 1: " + board[i][j]);
                    return false;
                }
            }
        }

        for (int i=0; i<board[0].length; i++) {
            Set<Character> presentInts = new HashSet<>();
            for (int j=0; j<board.length; j++) {
                if (board[j][i]>='1' && board[j][i] <= '9' && !presentInts.add(board[j][i])) {
                    System.out.println("False on stage 1: " + board[i][j]);
                    return false;
                }
            }
        }

        for (int i=0; i<board.length; i+=3) {
            for (int j=0; j<board[0].length; j+=3) {
                Set<Character> currBlockInts = new HashSet<>();
                for (int k=0; k<3; k++) {
                    for (int l=0; l<3; l++) {
                        if (board[i+k][j+l]>='1' && board[i+k][j+l] <= '9' &&!currBlockInts.add(board[i+k][j+l])) {
                            System.out.println("failed on stage 3:" + board[i+k][j+l]);
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
