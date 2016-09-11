# This function takes a list of lists, each with 2 positive integers [start,end] and returns the total sum of (end-start).
# Some of the starts/ends from different list elements may overlap.
# All list values are positive integers less than 2^30-1.

def answer(intervals):
    # sort pairs low to high by start time (pair = [start,end])
    intervals.sort(key=lambda x: x[0])
    total = 0
    
    # determine overlaps, modify, find difference, add to sum
    for i,val in enumerate(intervals):
        if i < (len(intervals)-1):
            if intervals[i][1]>intervals[i+1][1]:
                temp = intervals[i][1]
                intervals[i][1] = intervals[i+1][1]
                intervals[i+1][1] = temp
            if intervals[i][1]<intervals[i+1][0]:
                continue
            else:
                intervals[i][1]=intervals[i+1][0]
        total += intervals[i][1]-intervals[i][0]
    
    # return the sum
    return total