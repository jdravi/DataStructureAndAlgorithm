from pprint import pprint
class Node(object):

	def __init__(self,data):

		self.left = None
		self.right = None
		self.data = data




class Tree(object):
	"""docstring for Tree"""
	def __init__(self,data):
		
		self.root = Node(data)
		self.head = None
		self.prev = None

	def get_node(self,data):

		return Node(data)

	def preorder(self,root):

		if(root is not None):
			print(root.data)
		else:

			self.preorder(root.left)
			self.preorder(root.right)

	def inorder(self,root):

		if root is not None:
			self.inorder(root.left)
			print(root.data)
			self.inorder(root.right)

	def tree_to_dll(self,root):
		if root is None:
			return
		else:
			self.tree_to_dll(root.left)
			if self.prev is None:
				self.head = root
			else:
				root.left = self.prev
				self.prev.right = root
			self.prev = root
			self.tree_to_dll(root.right)





	def mod_sum(self,root):

		if root.left==None and root.right==None:
			temp = root.data


	def print(self):
		while self.head is not None:
			print(self.head.data,end = " ")
			self.head = self.head.right






if __name__ == '__main__':

	t  = Tree(2)

	t.root.left = Node(1)
	t.root.right = Node(3)
	# t.root.left.left = Node(25)
	# t.root.left.right = Node(30)
	# t.root.right.left = Node(36)

	t.tree_to_dll(t.root)
	t.print()
