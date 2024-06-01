class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int i= 0;
        List<int[]> newIntervals = new ArrayList<int[]>();

        while(i<intervals.length && intervals[i][1] < newInterval[0]){
            newIntervals.add(intervals[i]);
            i++;
        }

        while(i<intervals.length && intervals[i][0] <= newInterval[1]){
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
            i++;
        }
        
        newIntervals.add(newInterval);

        while(i<intervals.length){
            newIntervals.add(intervals[i]);
            i++;
        }

        int[][] result = new int[newIntervals.size()][2];
        int currentIndex = 0;
        for(i=0; i<newIntervals.size(); i++){
            result[currentIndex] = newIntervals.get(i);
            currentIndex++;
        }
        
        return result;
    }
}