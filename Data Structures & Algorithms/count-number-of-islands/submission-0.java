class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i=0; i<grid[0].length; i++) {
            for (int j=0; j<grid.length; j++) {
                if (grid[j][i] == '1') {
                    check(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }

    private void check(char[][] grid, int i, int j) {
        int result = 0;
        grid[j][i] = '0';
        if ((i > 0) && (grid[j][i-1] == '1')) {
            check(grid, i-1, j);
        }
        if ((j > 0) && (grid[j-1][i] == '1')) {
            check(grid, i, j-1);
        }
        if ((j < grid.length - 1) && (grid[j+1][i]) == '1') {
            check(grid, i, j+1);
        }
        if ((i < grid[0].length - 1) && (grid[j][i+1]) == '1') {
            check(grid, i+1, j);
        }
        return;
    }
}
