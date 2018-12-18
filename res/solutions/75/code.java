public class Solution {
    public void sortColors(int[] nums) {
        int i = 0;
        int j = 0;
        for (int k = 0; k < nums.length; ++k) {
            int v = nums[k];
            nums[k] = 2;
            if (v < 2) nums[j++] = 1;
            if (v == 0) nums[i++] = 0;
        }
    }
}
