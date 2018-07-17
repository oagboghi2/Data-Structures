import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    return self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    count = 0
    if self.size <= 0: return 0

    while self.storage.head.get_next() != None:
      count += 1
      current = self.storage.head.get_next()
      if current == None:
        return count
      else:
        return False
    
