from PythonCode.LinkedList.node import Node


class LinkedList():
    def __init__(self):
        self.head = None
        self.k = 0

    def add_beg(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head.next
            self.head = node

    def kth_node_from_end(self,head,from_end):

        if head is not None:
                self.kth_node_from_end(head.next,from_end)
                self.k = self.k + 1
                if self.k == from_end:
                    print(head.data)
    def kth_node_method2(self,head,from_end):


        start = head
        end = head
        count = 0


        while count<from_end:
            end = end.next
            count = count+1

        while end!=None:

            start = start.next
            end = end.next

        print(start.data)












node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_1.next = node_2
node_2.next = node_3

ll = LinkedList()
ll.head = node_1
ll.kth_node_from_end(ll.head,3)
ll.kth_node_method2(ll.head,3)