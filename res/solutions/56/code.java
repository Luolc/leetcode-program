public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        intervals.sort(Cmp.getInstance());

        List<Interval> ans = new LinkedList<>();

        Interval cur = null;
        for (Interval interval : intervals) {
            if (cur == null) {
                cur = interval;
                continue;
            }

            if (interval.start > cur.end) {
                ans.add(new Interval(cur.start, cur.end));
                cur = interval;
            } else {
                cur.end = Math.max(cur.end, interval.end);
            }
        }

        if (cur != null) ans.add(new Interval(cur.start, cur.end));

        return ans;
    }

    private static class Cmp implements Comparator<Interval> {
        private static final Cmp instance = new Cmp();

        static Cmp getInstance() {
            return instance;
        }

        private Cmp() {
        }

        @Override
        public int compare(Interval i1, Interval i2) {
            return i1.start - i2.start;
        }
    }
}
