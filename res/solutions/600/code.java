public class Solution {
    public int findIntegers(int num) {
        // fib[k]: valid counts with length = k
        int[] fib = new int[32];
        fib[0] = 1;
        fib[1] = 2;
        for (int i = 2; i < 32; ++i) fib[i] = fib[i - 1] + fib[i - 2];

        List<Integer> digits = new LinkedList<>();
        while (num > 0) {
            digits.add(num % 2);
            num /= 2;
        }

        int ans = 0;
        for (int i = digits.size() - 1; i >= 0; --i) {
            ans += digits.get(i) * fib[i];
            if (i == digits.size() - 1 || digits.get(i) == 0 || digits.get(i + 1) == 0) continue;

            --ans;
            break;
        }

        return ans + 1;
    }
}
