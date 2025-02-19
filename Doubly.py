class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

      class DoublyLinkedList:
         def __init__(self):
            self.head = None

         def insert(self,data):
            new_node = Node(data)
            if self.head:
               self.head.prev = new_node
               new_node.next = self.head

         def dispaly(self):
            temp = self.head
            while temp:
               print(temp.data, end="->")
               temp = temp.next
               print("None")

     #Example Usage
      ll = DoublyLinkedList()
      ll.insert(10)
      ll.insert(20)
      ll.insert(30)
      ll.display()