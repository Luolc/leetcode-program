Sort the intervals by their `start` value.
Keep Enlarging the interval at the left until the left boundary of the next interval is larger than 
the right boundary of current maintained interval.
Then add current interval to the answer list.
Repeat until reaching the end.
