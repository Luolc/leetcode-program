This is a two pointers problem.

First, we can easily prove the following facts:
- The boundaries of the range should be in the given numbers.

If we were maintaining a set, which contains k numbers, each belongs to an independent row. 
Then selecting the smallest and biggest number in the set as the boundaries and this would be a valid range obviously. 
So now we just need to search all the sets and find the smallest range.
This set can be maintained with two pointers.

Initially, creates
- a heap which contains the pointer to first element (also means smallest number) of each row.
- a `max` variable, indicates the max value of the heap
- a `range` variable, indicates the current optimal answer's range size, INF initially

In a loop,
- takes and removes the top of the heap, records as `top`, and calculates the `max` minus `top`
- if the result is smaller than the current answer's, then update `range`
- add the next element of `top` if it has a next, otherwise break the loop

Then we would get the optimal answer.
