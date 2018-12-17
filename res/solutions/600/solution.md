This is a DP problem.

**Step 1**: build a sequence `f` where `f[k]` indicates the count of binary number without consecutive `1`.

Indeed, `f` is the Fibonacci sequence.
For instance, `f[5]` is the count within `00000` to `11111`, which consists of two following parts:
- `00000` to `01111`; and
- `10000` to `10111`.

Note that numbers start with `11` are invalid.
The first part is `f[4]` and the second part is `f[3]`, thus `f[5] = f[4] + f[3]`.

**Step 2**: go through the digits of the given number from left to right, adds the count in 
corresponding sub-range, until encountered a consecutive `1`.
See the code for details.

Finally, add one to include the number itself.
