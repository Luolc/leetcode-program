public class Solution {
    public void nextPermutation(int[] nums) {
        for (int i = nums.length - 1; i >= 0; --i) {
            if (i != 0 && nums[i - 1] >= nums[i]) continue;

            if (i != 0) {
                int next = Integer.MAX_VALUE;
                int pos = -1;

                for (int j = i; j < nums.length; ++j) {
                    if (nums[j] > nums[i - 1] && nums[j] <= next) {
                        next = nums[j];
                        pos = j;
                    }
                }

                if (pos != -1) {
                    nums[pos] = nums[i - 1];
                    nums[i - 1] = next;
                }
            }

            for (int l = i, r = nums.length - 1; l < r; ++l, --r) {
                int t = nums[l];
                nums[l] = nums[r];
                nums[r] = t;
            }

            break;
        }
    }
}
