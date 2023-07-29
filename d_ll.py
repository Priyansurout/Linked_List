# Creating a Node
class Node:
  def __init__(self, data=None,prev=None):
    self.data = data
    self.next = None
    self.prev = prev

# Creating a LinkList
class DoublyLinkedList:
  def __init__(self, head=None):
    self.head = head

# Appending Nodes in LinkList(Add Data in Laste)
  def append(self, new_data):
     current = self.head
     if current is not None:
        while current.next:
          current = current.next
        current.next = new_data
        new_data.prev = current
        new_data.next = None
     else:
       new_data.prev = None
       self.head = new_data
  
  def prepend(self, new_data):
    if self.head is None:
      new_data.prev = None
      self.head = new_data
    else:
      self.head.prev = new_data
      new_data.next = self.head
      self.head = new_data
      new_data.prev = None


  def print(self):
    current = self.head
    if self.head:
      llstr = ''
      while current:
        llstr += str(current.data) + "<---->"if current.next else str(current.data)
        current = current.next
      print(llstr)
    else:
      print("Your LinkedList is Empty")