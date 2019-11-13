from PythonCode.LinkedList.node import Node
from PythonCode.LinkedList.LinkedList import LinkedList


class MergeTwoLinkedList:


    def find_sum(self,head1,head2,n1,n2):


        pass




    def get_size(self,head):

        count = 0
        while head!=None:
            count = count+1
            head = head.next
        return count

    def merge_util(self,head1,head2):

        n1= self.get_size(head1)
        n2 = self.get_size(head2)









