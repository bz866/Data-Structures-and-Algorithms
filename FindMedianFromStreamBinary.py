# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Find the median from the data stream
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minPart = [] # Simulate the behavior of MaxHeap
        self.maxPart = [] # Simulate the behavior of MinHeap
    
    """Find the inseart location by binary search
    Find: O(1)
    addNum: O(logn)
    """
    def binarySearchInsertLocation(self, minHeap, val, start, end):
        if start == end:
            if minHeap[start] > val:
                return start
            else:
                return start + 1
            
        if start > end:
            return start
        
        mid = (start + end ) // 2
        if minHeap[mid] < val:
            return self.binarySearchInsertLocation(minHeap, val, mid+1, end)
        elif minHeap[mid] > val:
            return self.binarySearchInsertLocation(minHeap, val, start, mid-1)
        else:
            return mid

    def addNum(self, num: int) -> None:
        # if the upper part is empty OR the num > the minimum of the upper part
        if (len(self.maxPart) == 0 or num > self.maxPart[0]):
            # rebalance if difference of two parts is larger than one
            if (len(self.maxPart) > len(self.minPart)):
                self.minPart.append(self.maxPart.pop(0))
            loc = self.binarySearchInsertLocation(self.maxPart, num, 0, len(self.maxPart)-1)
            self.maxPart.insert(loc, num)
            
        # if the lower part is empty OR the num < the maximum of the lower part
        elif (len(self.minPart) == 0 or num < self.minPart[-1]):
            # rebalance if difference of two parts is larger than one
            if (len(self.minPart) > len(self.maxPart)):
                self.maxPart.insert(0, self.minPart.pop(-1))
            loc = self.binarySearchInsertLocation(self.minPart, num, 0, len(self.minPart)-1)
            self.minPart.insert(loc, num)
        
        # if the maximum of the lower part <= num <= the minimum of the upper part 
        else:
            if (len(self.minPart) < len(self.maxPart)):
                self.minPart.append(num)
            else:
                self.maxPart.insert(0, num)
        

    def findMedian(self) -> float:
        if (len(self.minPart) > len(self.maxPart)):
            return self.minPart[-1]
        elif (len(self.minPart) < len(self.maxPart)):
            return self.maxPart[0]
        elif (len(self.maxPart) == len(self.minPart) == 0):
            return 0
        else:
            median = (self.minPart[-1] + self.maxPart[0]) / 2
            return median
