class ListNode:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt
    
    # 把 node 加在 self 节点之后
    def add(self, node):
       nxt = self.next
       self.next = node
       node.prev = self
       node.next = nxt 

    def remove(self, node):
        nxt = node.next
        if nxt:
            nxt.prev = self
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.head = ListNode(None, None) # 头节点
        self.tail = ListNode(None, None) # 尾部节点
        self.head.add(tail)
        self.key2node = {}


    def get(self, key: int) -> int:
        if key not in self.key2node: return -1
        node = self.key2node[key]
        item = node.val
        self.renew(node)
        return item

    # 更新 node 
    def renew(self, node):
        node.prev.remove(node)
        self.head.add(node)



    def put(self, key: int, value: int) -> None:
        if key  in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.renew(node)
        else:
            if self.cap == 0:
                tmp = self.tail.prev.prev
                tmp.next = self.tail
                self.tail.prev = tmp
                self.cap = 1
            
            node = ListNode(key, value)
            self.key2node[key] = node
            self.head.add(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)