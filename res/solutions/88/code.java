public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        long n = Math.round(Math.pow(2, nums.length));

        List<List<Integer>> ans = new LinkedList<>();

        for (int i = 0; i < n; ++i) {
            List<Integer> subset = new LinkedList<>();
            for (int j = 0; j < nums.length; ++j) {
                if ((i & (1 << j)) > 0) subset.add(nums[j]);
            }
            ans.add(subset);
        }

        return ans;
    }
}
