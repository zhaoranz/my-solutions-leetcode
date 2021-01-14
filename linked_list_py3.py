#how to create linked_list in python3
class Node(object):
     def __init__(self, item):
         self.item = item
         self.next =None
         
class SingleLinkList(object):
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def length(self):
        cur =self._head
        count = 0
        while cur is  not None:
            count +=1
            cur =cur.next
        return count
    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next
     def add_head(self, item):
          node = Node(item)
          node.next=self._head
          self._head = node
     def append(self, item):
          node = Node(item)
          if self.is_empty():
               self._head = node
          else:
               cur =self._head
               while cur.next is not None:
                    cur = cur.next
               cur.next =node
     def insert(self, index, item):
          if index <=0:
               self.add(item)
          elif index >(self.length() - 1):
               self.append_(item)
          else:
               node = Node(item)
               cur = self._head
               for i in range(index-1):
                    cur = cur.next
               node.next = cur.next
               cur.next = node
     def remove(self, item):
          cur =self._head
          pre =None
          while cur is not None:
               if cur.item ==item:
                    if not pre:
                         self._head = cur.next
                    else:
                         pre.next=cur.next
                    return True
               else:
                    pre = cur
                    cur = cur.next
     def find(self, item):
          return item in self.items()
               
            
if __name__ == "__main__":
    link_list = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    link_list._head =node1
    node1.next = node2

    print(link_list._head.item)
    print(link_list._head.next.item)
    



#Circular linked list
# define nodes:
class Node(object):
     def __init__(self, item):
          self.item = item
          self.next = None
class SingleCycleLinkList(object):
     def __init__(self):
          self._head = None
     def is_empty(self):
          return self._head is None
     def length(self):
          if self.is_empty():
               return 0
          count = 1
          cur =self._head()
          while cur.next != self._head():
               count += 1
               cur = cur.next
          return count
     def items(self):
          if self.is_empty():
               return
          cur = self._head
          while cur.next =! self._head:
               yield cur.item
               cur = cur.next
               yield cur.item
     def add(self, item):
          node = Node(item)
          if self.is_empty():
               self._head = None
               node.next = self._head
          else:
               node.next = self._head
               cur = self._head
               while cur.next != self._head():
                    cur = cur.next
               cur.next = node
          self._head = node

     def append(self, item):
          node =Node(item)
          if self.is_empty():
               self._head = node
               node.next = self._head
          else:
               cur = self._head
               while cur.next != self._head:
                    cur = cur.next
               cur.next = node
               node.next = self._head()
     def insert(self, index, item):
          if index <= 0 :
               self.add(item)
          elif index > self.length() -1:
               self.append(item)
          else:
               node = Node(item)
               cur = self._head()
               for i in range(index - 1):
                    cur = cur.next
               node.next = cur.next
               cur.next = node
     def remove(self, item):
          if self.is_empty():
               return
          cur = self._head
          pre = Node
          if cur.item == item:
               if cur.next != self._head:
                    while cur.next != self._head:
                         cur = cur.next
                    cur.next = self._head.next
                    self._head = self._head.next
               else:
                    self._head = None
          else:
               pre = self._head
               while cur.next != self._head:
                    if cur.item == item:
                         pre.next = cur.next
                         return True
                    else:
                         pre = cur
                         cur = cur.next
          if cur.item == item:
               pre.next = self._head
               return True
     def find(self, item):
          return item in self.items()


