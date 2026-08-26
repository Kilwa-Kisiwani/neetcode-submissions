class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Arrays.sort(nums);
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> a.getValue() - b.getValue());
        int curr = nums[0];
        int count = 0;
        for (int i=0; i<nums.length; i++) {
            if (curr != nums[i]) {
                // case 1: empty pq
                if (pq.size() < k) {
                    pq.add(new AbstractMap.SimpleEntry(curr, count));
                } else {
                    if (pq.peek().getValue() < count) {
                        pq.poll();
                        pq.add(new AbstractMap.SimpleEntry(curr, count));
                    }
                }
                curr = nums[i];
                count = 0;
            }
            count++;
        }


                if (pq.size() < k) {
                    pq.add(new AbstractMap.SimpleEntry(curr, count));
                } else {
                    if (pq.peek().getValue() < count) {
                        pq.poll();
                        pq.add(new AbstractMap.SimpleEntry(curr, count));
                    }
                }
        int size = pq.size();
        int[] result = new int[size];
        for (int i=0; i<size; i++) {
            result[i] = pq.poll().getKey();
        }
        return result;
    }

}
