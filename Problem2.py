# Time Complexity : O(1) as node insertion, node deletion, finding node is done in constant time
# Space Complexity :O(n) where n is maximum number of items inserted in doubly linkedlist
# Did this code successfully run on Leetcode :Yes
# Any problem you faced while coding this : No




class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dct = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dct:
            return -1
        self.remove(self.dct[key])
        self.add(self.dct[key])
        return self.dct[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dct:
            self.remove(self.dct[key])
            self.add(self.dct[key])
            self.dct[key].value = value
        else:
            node = Node(key, value)
            self.dct[key] = node
            self.add(node)

        if len(self.dct) > self.capacity:
            n = self.tail.prev
            self.remove(n)
            del self.dct[n.key]

    def add(self, node):
        n = self.head.next
        self.head.next = node
        n.prev = node
        node.next = n
        node.prev = self.head

    def remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p
        node.next = node.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# In this problem, I first created a class for the attributes of doubly linked lst. Then I initiallized a head and tail node.
# For Each put, it is inserted at head and is added to dictionary. For each get item is checked and if it is preset in dictionary,
# it is added to front. If the Length of the dicitionary increases, then the tail item is removed.