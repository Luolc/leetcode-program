### Solution 1: DP

Use `sum[i]` to represents the maximum subarray that ends with the `i`-th number `nums[i]`.
See the code for details.

### Solution 2: Divide and Conquer

Divide a sequence of number `a` to two parts: `a[:mid]` and `a[mid:]`.
The answer may be found in the following three cases:
- the maximum subarray of `a[:mid]`,
- the maximum subarray of `a[mid:]`, and
- the concatenation of: the maximun subarray of `a[:mid]` ending with the `mid - 1`-th element, 
and the maximum subarray of `a[mid:]` starting with the `mid`-th element.

This is an `O(log(N))` algorithm.
