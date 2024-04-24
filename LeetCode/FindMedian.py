"""Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value, and the median is the mean of the two
middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data
structure.
double findMedian() returns the median of all elements so far. Answers within
10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling
findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
"""
import bisect
# from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.vals = []
        # self.vals = SortedList()

    def addNum(self, num: int) -> None:
        bisect.insort(self.vals, num)
        # self.vals.add(num)

    def findMedian(self) -> float:
        s = len(self.vals)
        if s % 2 == 0:
            return (self.vals[s//2 - 1] + self.vals[s//2]) / 2
        else:
            return self.vals[s//2]


test_cases = [1, 2, 3]
# test_cases = [0, 0]
obj = MedianFinder()
for num in test_cases:
    obj.addNum(num)
    print(obj.findMedian())

"""
Time complexity:
    The overall time complexity of this code is:
    - O(n) for adding a number.
        Since the list self.vals potentially grows with each call to
        addNum, the time complexity of adding a number using
        bisect.insort can be considered O(n) in the worst case when
        considering the linear scan to find the insertion position in
        addition to the logarithmic time complexity of the binary search
        performed by bisect.insort.
    - O(1) for finding the median.
        The time complexity of the findMedian method is O(1) because
        it involves simple arithmetic operations to calculate the median
        using the sorted list self.vals. The length of self.vals is used
        to determine whether the number of elements is odd or even, and
        then the median is calculated accordingly.

Space complexity:
    The space complexity depends on the space required to store the list
    self.vals, which contains all the numbers added to the data structure.
    - Space required for the list self.vals:
        As numbers are added to the MedianFinder object, they are stored
        in the self.vals list. Therefore, the space required for self.vals
        grows with the number of elements added to the data structure. In
        the worst case, if all elements are distinct, the space complexity
        is O(n), where n is the number of elements added to the list.
    - Additional space:
        Apart from the list self.vals, there are no other significant data
        structures or variables that grow with the input size. Thus, they
        contribute only a constant amount of space, resulting in a space
        complexity of O(1).
    Therefore, the overall space complexity of the MedianFinder class is
    O(n), where n is the number of elements added to the list self.vals.

https://leetcode.com/problems/find-median-from-data-stream/solutions/5015759/sorted-list/
    Runtime: 919 ms (Beats 12.95% of users with Python3)
    Memory: 38.00 MB (Beats 91.63% of users with Python3)
"""
