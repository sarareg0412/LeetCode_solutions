class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        newIntervals = []
        i = 0
        # Before finding intersection loop
        while i <len(intervals) and intervals[i][1] < newInterval[0]:
            newIntervals.append(intervals[i])
            i += 1
        
        while i<len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), 
                           max(intervals[i][1], newInterval[1])]
            i += 1

        newIntervals.append(newInterval)
        # After merging loop
        while i <len(intervals):
            newIntervals.append(intervals[i])
            i += 1

        return newIntervals
                    