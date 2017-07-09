public class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        List<Node> rows = nums.stream().map(row -> {
            Iterator<Integer> it = row.iterator();
            Node start = new Node(it.next());
            Node node = start;
            while (it.hasNext()) {
                Node next = new Node(it.next());
                node.next = next;
                node = next;
            }
            return start;
        }).collect(Collectors.toList());
        PriorityQueue<Node> heap = new PriorityQueue<>(rows);
        int[] ret = null;
        int range = Integer.MAX_VALUE;
        int max = rows.stream().mapToInt(raw -> raw.v).max().getAsInt();
        while (true) {
            Node top = heap.poll();
            if (max - top.v < range) {
                range = max - top.v;
                ret = new int[]{top.v, max};
            }
            if (top.next != null) {
                max = Math.max(max, top.next.v);
                heap.add(top.next);
            } else {
                break;
            }
        }

        return ret;
    }

    private static class Node implements Comparable<Node> {
        int v;

        Node next;

        Node(int v) {
            this.v = v;
        }

        @Override
        public int compareTo(Node o) {
            return v - o.v;
        }
    }
}
