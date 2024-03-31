class BSTNode:
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right

	def __str__(self):
		return f"{self.data}"

	def __repr__(self):
		return f"{self.data}"

class BST:
	def __init__(self, root=None):
		self.root=root
		self.contents = []

	def __str__(self):
		if self.root == None:
			return "The tree is empty"
		else:
			self.output = ""
			self.print_tree(node=self.root)
			return self.output

	def __repr__(self):
		if self.root == None:
			return "The tree is empty"
		else:
			self.output = ""
			self.print_tree(node=self.root)
			return self.output

	def print_tree(self, node, level=0):
		if node != None:
			self.print_tree(node.right, level + 1)
			self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
			self.print_tree(node.left, level + 1)

	def add(self, node):
		if type(node) != int and type(node) != BSTNode:
			raise ValueError("You must pass an int or a BSTNode")

		if type(node) == int:
			node = BSTNode(node)

		if node in self.contents:
			return

		if self.root == None:
			self.root = node
			self.contents.append(node.data)
			return

		self.add_node(self.root, node)

	def add_node(self, current_node, new_node):
		if new_node.data > current_node.data:
			if current_node.right == None:
				current_node.right = new_node
				self.contents.append(new_node.data)
				return
			else:
				#recurse/traverse
				self.add_node(current_node.right, new_node)
		elif current_node.data > new_node.data:
			if current_node.left == None:
				current_node.left = new_node
				self.contents.append(new_node.data)
				return
			else:
				#recurse/traverse
				self.add_node(current_node.left, new_node)


#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)
print(bst)