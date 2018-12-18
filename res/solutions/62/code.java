public class Solution {
    private static int[][] C = new int[201][201];

    public int uniquePaths(int m, int n) {
        return computeC(m + n - 2, n - 1);
    }

    private static int computeC(int b, int u) {
        if (u == 0 || b == u) return 1;
        if (C[b][u] != 0) return C[b][u];
        return C[b][u] = computeC(b - 1, u) + computeC(b - 1, u - 1);
    }
}
