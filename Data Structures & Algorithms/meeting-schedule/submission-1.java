/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        if (intervals.isEmpty()) {
            return true;
        }
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));
        int startMin = intervals.get(0).start;
        int endMax = startMin;
        for (Interval interval : intervals) {
            if (interval.start < endMax || interval.end < endMax) {
                return false;
            }
            endMax = interval.end;

        }

        return true;
    }
}
