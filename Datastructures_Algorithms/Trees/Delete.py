class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise (ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        # Check if node has more than one child
        if node._left_child is not None and node._right_child is not None:
            raise ValueError('Cannot detach node with two children')

        node_parent = node._parent
        # check if child is right or left
        child = node._left_child if node._left_child is not None else node._right_child
        if child is not None:
            child._parent = node_parent

        # if node is not rootnode
        if node_parent is not None:
            if node_parent._left_child == node:
                node_parent._left_child = child
            else:
                node_parent._right_child = child

        # if node is rootnode
        else:
            self._root_node = child
        node._parent = None
        node._left_child = None
        node._right_child = None

    def delete_node(self, num):
        deleted_node = self._find(num)  # Etsi poistettava solmu

        if deleted_node is None:
            return  # Solmua ei löytynyt, ei tehdä mitään

        node_parent = deleted_node._parent

        # Jos poistettava solmu on juurisolmu
        if node_parent is None:
            # Käsittele juurisolmu erikseen
            if deleted_node._left_child and deleted_node._right_child:
                # Kaksi lasta -> etsitään in-order seuraaja
                successor = deleted_node._right_child
                while successor._left_child:
                    successor = successor._left_child

                deleted_node.data = successor.data  # Kopioi arvo
                self._detach_node(successor)  # Poista seuraaja solmusta
            else:
                # Yksi tai ei lasta
                self._root_node = deleted_node._left_child or deleted_node._right_child
                if self._root_node:
                    self._root_node._parent = None

        else:
            # Ei-juurisolmut
            if deleted_node._left_child and deleted_node._right_child:
                successor = deleted_node._right_child
                while successor._left_child:
                    successor = successor._left_child

                deleted_node.data = successor.data
                self._detach_node(successor)
            else:
                child_node = deleted_node._left_child or deleted_node._right_child
                if deleted_node == node_parent._left_child:
                    node_parent._left_child = child_node
                else:
                    node_parent._right_child = child_node
                if child_node:
                    child_node._parent = node_parent


tree = Tree()
tree.insert(50)
tree.insert(20)
tree.insert(70)
tree.insert(90)
tree.insert(10)
tree.insert(40)
tree.insert(30)
tree.insert(35)
tree.delete_node(50)
tree.delete_node(20)
tree.delete_node(70)
tree.delete_node(90)
tree.delete_node(10)
tree.delete_node(40)
tree.delete_node(30)
tree.delete_node(35)
print(tree._find(tree._root_node))