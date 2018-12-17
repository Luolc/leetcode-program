**Step 1**: search from the right to find the first `i` that satisfies `nums[i-1] < nums[i]`. 
Let `i = 0` if not found.

Note that `nums[i:]` is in descending order.

**Step 2** (apply only if `i != 0`): search `nums[i:]` from the left to find `nums[j]` that just larger than `nums[i-1]`. 
Choose the larger `j` if there are duplicates (to maintain the descending order). 
Swap `nums[i-1]` and `nums[j]`.

Note that `nums[i:]` is still in descending order after swaping.

**Step 3**: reverse `nums[i:]`.
