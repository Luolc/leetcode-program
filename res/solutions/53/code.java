public class Solution {
    public int maxSubArray(int[] nums) {
        // return solveWithDp(nums);
        return solveWithDivideAndConquer(nums, 0, nums.length).max;
    }

    private int solveWithDp(int[] nums) {
        int[] sum = new int[nums.length];
        sum[0] = nums[0];

        int ans = sum[0];
        for (int i = 1; i < nums.length; ++i) {
            if (sum[i - 1] < 0) sum[i] = nums[i];
            else sum[i] = sum[i - 1] + nums[i];
            ans = Math.max(ans, sum[i]);
        }

        return ans;
    }

    private Subarray solveWithDivideAndConquer(int[] nums, int l, int r) {
        if (l + 1 == r) return new Subarray(nums[l]);

        int mid = (l + r) / 2;
        Subarray left = solveWithDivideAndConquer(nums, l, mid);
        Subarray right = solveWithDivideAndConquer(nums, mid, r);

        int leftMax = Math.max(left.leftMax, left.sum + right.leftMax);
        int rightMax = Math.max(right.rightMax, right.sum + left.rightMax);
        int max = Math.max(left.rightMax + right.leftMax, Math.max(left.max, right.max));
        int sum = left.sum + right.sum;

        return new Subarray(leftMax, rightMax, max, sum);
    }

    private static class Subarray {
        int leftMax;
        int rightMax;
        int max;
        int sum;

        Subarray(int value) {
            leftMax = value;
            rightMax = value;
            max = value;
            sum = value;
        }

        Subarray(int leftMax, int rightMax, int max, int sum) {
            this.leftMax = leftMax;
            this.rightMax = rightMax;
            this.max = max;
            this.sum = sum;
        }
    }
}
