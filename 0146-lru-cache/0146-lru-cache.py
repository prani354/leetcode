class LRUCache:
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)  #Dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def addnode(self,newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode
        
        

    def deletenode(self,delnode):
        prevv = delnode.prev
        nextt = delnode.next
        prevv.next = nextt
        nextt.prev = prevv        

    def get(self, key: int) -> int:
        if key in self.map:  # the key is the node value and value is the address of that node
            resnode = self.map[key]
            ans = resnode.val
            del self.map[key]
            self.deletenode(resnode)
            self.addnode(resnode)
            self.map[key] = self.head.next  # Storing the address that is why using pointer
            return ans

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            currnode = self.map[key]
            del self.map[key]
            self.deletenode(currnode)

        if len(self.map) == self.capacity:
            del self.map[self.tail.prev.key]
            self.deletenode(self.tail.prev)

        self.addnode(self.Node(key,value))  #creating the node
        self.map[key] = self.head.next

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)