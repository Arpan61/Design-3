# Time Complexity : O(n) where n is number of elements in list
# Space Complexity :O(n) where n is number of elements in list
# Did this code successfully run on Leetcode :Yes
# Any problem you faced while coding this : No


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = []
        self.fillList(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0

    def fillList(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                self.queue.append(i.getInteger())
            else:
                self.fillList(i.getList())

            # Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())