"""
Module realize some of data structures:
Linked List
Queue
Stack
Hash Table
Binary Search Tree
Graph
"""
import logging
import sys


class DeleteError(Exception):
    """
    Exception that raises when delete method cant removes element
    """

    def __init__(self, msg: str):
        super().__init__()
        self.message = msg

    def __str__(self):
        return self.message


class EdgeError(Exception):
    """
    Exception that raises when method tries link vertex to unexisting vertex
    """

    def __init__(self, msg: str):
        super().__init__()
        self.message = msg

    def __str__(self):
        return self.message


class LLNode:
    """
    Class describes linked list node

    Attributes
    ----------
    next: LLNode pointer on the another node. Default value None
    data: some data stored in node
    """

    def __init__(self, data: 'any of primitive type'):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node<data={self.data}>"

    def __str__(self):
        return f"Node: {self.data}"


class LinkedList:
    """
    Class realize Linked list structure

    Methods
    -------
    prepend(data):
        adds node to the head position
    append(data):
        adds node to the tail position
    lookup(data): int
        returns index of element with data value or None
    insert(index: int):
        insert node in index position with right offset
    delete(index: ind):
        deletes element in given index

    Attributes
    head: LLNode, pointer on first node of list
    tail: LLNode, pointer on last node of list
    """
    logger = logging.getLogger("Linked list")
    c_handler = logging.StreamHandler(stream=sys.stdout)
    c_formatter = logging.Formatter("%(name)s - %(message)s ")
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    def __init__(self):
        self.head = None
        self.tail = None
        LinkedList.logger.info("List creates")

    def prepend(self, data):
        """Adds element to the start of list"""
        self.logger.info("<<<Prepend started>>>")
        node = LLNode(data)
        if self.head:
            node.next = self.head
            self.head = node
            self.logger.info("Node %s added to the start of list. Head %s, next %s ",
                             data, self.head, self.head.next)
            self.logger.info("<<<Prepend ends>>>")
        else:
            self.head = node
            self.tail = node
            self.logger.info("List is empty. Adds node %s."
                             "Head is %s. Tail is %s", data, self.head, self.tail)
            self.logger.info("<<<Prepend ends>>>")

    def append(self, data):
        """Adds element to the end of list"""
        self.logger.info("<<<Append started>>>")
        node = LLNode(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.logger.info("Node %s added to the end of list. Tail %s,",
                             data, self.head)
            self.logger.info("<<<Append ends>>>")
        else:
            self.head = node
            self.tail = node
            self.logger.info("List is empty. Adds node %s."
                             "Head is %s. Tail is %s", data, self.head, self.tail)
            self.logger.info("<<<Append ends>>>")

    def lookup(self, data) -> int:
        """
        Method  looks for element with  data value and returns its index.
        Return -1 if not found
        """
        self.logger.info("<<<Lookup started>>>")
        ind = 0
        node = self.head
        if not node:
            return -1
        while node:
            if node.data == data:
                self.logger.info("Element %s found in %d", data, ind)
                self.logger.info("<<<Lookup ends>>>")
                return ind
            node = node.next
            ind += 1
        if self.tail.data == data:
            self.logger.info("Element %s found in %d", data, ind)
            self.logger.info("<<<Lookup ends>>>")
            return ind
        self.logger.info("Element %s not found", data)
        self.logger.info("<<<Lookup ends>>>")

        return -1

    def value(self, index: int):
        """Returns item using index"""
        node = self.head
        count = 0
        while node:
            if count == index:
                return node.data
            node = node.next
            count += 1

    def insert(self, data, index: int):
        """
        Adds element data in index position
        If index is more than lists length adds to end of the list
        """
        self.logger.info("<<<Insert started>>>")
        node = LLNode(data)
        if not index:
            self.logger.info("The index is 0, adds  %s to the head of list", data)
            self.prepend(data)
            self.logger.info("<<<Insert ends>>>")
            return
        curr_ind = 1
        prev_node = self.head
        curr_node = prev_node.next
        while curr_node.next:
            if curr_ind == index:
                prev_node.next = node
                node.next = curr_node
                self.logger.info("Adds %s in position %s", data, curr_ind)
                self.logger.info("Prev: %s, cur: %s, next: %s", prev_node, node, curr_node)
                if not curr_node.next:
                    self.tail = curr_node
                    self.logger.info("Tail moved")
                self.logger.info("<<<Insert ends>>>")
                return
            prev_node = curr_node
            curr_node = curr_node.next
            curr_ind += 1
        self.logger.info("Cant find position, adds to the end")
        self.append(data)
        self.logger.info("<<<Insert ends>>>")

    def delete(self, index: int) -> bool:
        """
        Deletes an element of the list in index position
        :raise DeletionError if deletion is impossible
        """
        self.logger.info("<<<Delete started>>>")
        if not index:
            self.logger.info("Index %s, delete: %s", index, self.head)
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            self.logger.info("Head: %s", self.head)

            self.logger.info("<<<Delete ends>>>")
            return True
        if index < 0:
            raise DeleteError("No such position to delete")
        temp_index = 1
        prev_node = self.head
        curr_node = prev_node.next
        while curr_node.next:
            if temp_index == index:
                prev_node.next = curr_node.next
                self.logger.info("Deleting %s in position %s", curr_node, index)
                self.logger.info("Prev: %s, curr: %s", prev_node, prev_node.next)
                self.logger.info("<<<Delete ends>>>")
                return True
            prev_node = curr_node
            curr_node = curr_node.next
            temp_index += 1
        if temp_index == index:
            self.tail = prev_node
            self.logger.info("Deleting last element %s", curr_node)
            prev_node.next = None
            self.logger.info("Tail: %s next: %s", self.tail, self.tail.next)
            self.logger.info("<<<Delete ends>>>")
            return True

        raise DeleteError("No such position to delete")

    def print_list(self):
        """Prints all elements of list"""
        print(f"Head| {self.head.data}-->", end=" ")
        curr = self.head.next
        if not curr:
            return
        while curr.next:
            print(f"{curr.data}-->", end=" ")
            curr = curr.next
        print(f"{self.tail.data} |Tail")


class Queue:
    """
    Class realize queue data structure
    Methods
    -------
    enqueue(data):
        Adds element to the end of queue
    dequeue(data): LLNode
        Removes and return element from the right side of queue
    peek(): LLNode
        Returns element from the right side without deletion

    Attributes:
    front: LLNode right side of queue(beginning)
    rear: LLNode ends of queue
    """
    logger = logging.getLogger("Queue")
    c_handler = logging.StreamHandler(stream=sys.stdout)
    c_formatter = logging.Formatter("%(name)s - %(message)s ")
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    def __init__(self):
        self._front = None
        self._rear = None
        logger = logging.getLogger("Linked list")
        logger.setLevel(logging.WARNING)
        self.list = LinkedList()

        self.logger.info("The queue creates")

    def enqueue(self, data):
        """Adds node to te end of queue"""
        self.logger.info("<<<Enqueue started>>>")
        self.list.prepend(data)
        self.logger.info("Adds %s to end of queue", data)
        self._front = self.list.tail
        self._rear = self.list.head
        self.logger.info("Front: %s", self._front)
        self.logger.info("Rear: %s", self._rear)
        self.logger.info("<<<Enqueue ends>>>")

    def dequeue(self):
        """Removes element from the front of a queue"""
        self.logger.info("<<<Dequeue started>>>")
        node = self._front
        data = node.data
        self.logger.info(">Removes %s", node)
        index = self.list.lookup(data)
        self.list.delete(index)
        self._front = self.list.tail
        self._rear = self.list.head
        self.logger.info("Front: %s", self._front)
        self.logger.info("Rear: %s", self._rear)
        self.logger.info("<<<Dequeue ends>>>")
        return node

    def peek(self):
        """Returns element from  the end of a queue without deletion"""
        return self._front


class Stack:
    """
    Class realize stack structure

    Methods
    -------
    push(data):
        adds node to the top of a stack
    pop(data): LLnode
        pops top element from the stack
    peek(): LLnode
        returns top element of the stack
        without deletion
    """
    logger = logging.getLogger("Stack")
    c_handler = logging.StreamHandler(stream=sys.stdout)
    c_formatter = logging.Formatter("%(name)s - %(message)s ")
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    def __init__(self):
        self.list = LinkedList()
        self.top = self.list.tail
        logger = logging.getLogger("Linked list")
        logger.setLevel(logging.WARNING)
        self.logger.info("Stack creates")

    def push(self, data):
        """Push node with data to the stack"""
        self.logger.info("<<<Push started>>>")
        self.list.append(data)
        self.top = self.list.tail
        self.logger.info("Element %s added.\n"
                         "Top of the stack %s", data, self.top)
        self.logger.info("<<<Push ends>>>")

    def pop(self):
        """Pops element from list"""
        node = self.top
        self.logger.info("<<<Pop started>>>")
        self.logger.info("Top node %s", node)
        index = self.list.lookup(node.data)
        self.list.delete(index)
        self.top = self.list.tail
        self.logger.info("Node pops, top node now %s", self.top)
        self.logger.info("<<<Pop ends>>>")
        return node

    def peek(self):
        """Returns top element of the stack """
        return self.top


class BucketNode:
    """Node with a hash index for the HashTable """

    def __init__(self, key, value):
        self.hash = hash(key)
        self.key = key
        self.value = value

    def get_key(self):
        """Returns key of node"""
        return self.key

    def get_value(self):
        """Returns value of node"""
        return self.value


class HashTable:
    """
    Class realize Hash table
    Methods
    ------
    insert(key, value):
        adds pair key, value to the table
    lookup(key): data
        returns a data for  the specified key
    delete(key):
        removes node with  a specified key from the table
        :raise DeleteError if deletion is impossible

    """
    logger = logging.getLogger("Hash table")
    c_handler = logging.StreamHandler(stream=sys.stdout)
    c_formatter = logging.Formatter("%(name)s - %(message)s ")
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    def __init__(self):
        log = logging.getLogger("Stack")
        log.setLevel(logging.WARNING)
        self.buckets = LinkedList()
        self.logger.info("Hash table created")

    def insert(self, key, value):
        """Insert  key value in table and resolving collisions"""
        self.logger.info("Insert starts >>>>>")
        node = BucketNode(key, value)
        curr = self.buckets.head
        flag = True
        curr_hash = hash(key)
        while curr:
            if curr.data.hash == curr_hash:
                if curr.data.key == key:
                    self.logger.info("Updates %s > %s", curr.data.value, value)
                    curr.data.value = value
                    return
                self.logger.info("Collision found! Hash in table %s equals new %s",
                                 curr.data.hash, curr_hash)
                flag = False
                tmp_node = BucketNode(curr.data.key, curr.data.value)
                if not isinstance(curr.data.value, LinkedList):
                    curr.data.value = LinkedList()
                    self.logger.info("New list created")
                curr.data.value.append(tmp_node)
                curr.data.value.append(node)
            curr = curr.next
        if flag:
            self.buckets.append(node)
        self.logger.info("Insert ends >>>>>")

    def lookup(self, key):
        """Returns value from key"""
        curr_hash = hash(key)
        curr_node = self.buckets.head
        while curr_node:
            if curr_node.data.hash == curr_hash:
                if not isinstance(curr_node.data.value, LinkedList):
                    self.logger.info("Found key: %s ,value: %s", key,
                                     curr_node.data.value)
                    return curr_node.data.value

                self.logger.info("Collision resolving found")
                inner_node = curr_node.data.value.head
                while inner_node:  # enters to the inner list
                    self.logger.info(inner_node.data.value)
                    if inner_node.data.key == key:
                        self.logger.info("Found key: %s, value: %s", key,
                                         inner_node.data.value)
                        return inner_node.data.value
                    inner_node = inner_node.next
            curr_node = curr_node.next
        return -1

    def delete(self, key):
        """Method deletes element from table"""
        curr_hash = hash(key)
        prev_node = self.buckets.head
        if prev_node.data.hash == curr_hash:
            self.logger.info("Hash found")
            if not isinstance(prev_node.data.value, LinkedList):
                self.logger.info("Removing %s", self.buckets.head.data.value)
                self.buckets.head = prev_node.next
                return True
            inner_node = prev_node.data.value.head
            self.logger.info("Enter to the inner list")
            if inner_node.data.key == key:
                self.logger.info("Key found in inner list")
                self.logger.info("Removing %s", inner_node.data.value)
                inner_node.data.value.head = inner_node.next
                return
            while inner_node:  # enters to the inner list
                if inner_node.next.data.key == key:
                    if inner_node.next.next:
                        inner_node.next = inner_node.next.next
                        self.logger.info("Key found in inner list")
                        self.logger.info("Removing %s", inner_node.data.value)
                        return True
                    self.logger.info("Key found in inner list")
                    self.logger.info("Removing %s", inner_node.data.value)
                    inner_node.tail = inner_node
                    return True
                inner_node = inner_node.next

        curr_node = prev_node.next
        while curr_node:
            if curr_node.data.hash == curr_hash:
                if not isinstance(curr_node.data.value, LinkedList):
                    self.logger.info("Removing %s", curr_node.data.value)
                    prev_node.next = curr_node.next
                    return True
                else:
                    self.logger.info("Enter to the inner list")
                    if inner_node.data.key == key:
                        self.logger.info("Key found in inner list")
                        self.logger.info("Removing %s", inner_node.data.value)
                        inner_node.data.value.head = inner_node.next
                        return
                    while inner_node:  # enters to the inner list
                        if inner_node.next.data.key == key:
                            if inner_node.next.next:
                                inner_node.next = inner_node.next.next
                                self.logger.info("Key found in inner list")
                                self.logger.info("Removing %s", inner_node.data.value)
                                return True
                            self.logger.info("Key found in inner list")
                            self.logger.info("Removing %s", inner_node.data.value)
                            inner_node.tail = inner_node
                            return True
                        inner_node = inner_node.nex
            curr_node = curr_node.next
        raise DeleteError("Noting to delete")


class Node:
    """Class implements node for binary search tree"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        """Return node data"""
        return self.data

    def __setattr__(self, key, value):
        """Checks data type"""
        if key == "data" and not isinstance(value, int):
            raise ValueError("Data should be integer")
        self.__dict__[key] = value


class BST:
    """
    Class implements binary search tree

    Methods
    -------
    insert(data:int):
        inserts a node to the tree
    lookup(data:int): Node
        Looks for node and return pointer on it
    delete(data: int):
        removes element

    Attributes
    ---------
    root: Node root of a tree
    """
    logger = logging.getLogger("Tree")
    c_handler = logging.StreamHandler(stream=sys.stdout)
    c_formatter = logging.Formatter("%(name)s - %(message)s ")
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    def __init__(self):
        log = logging.getLogger("Hash table")
        log.setLevel(logging.WARNING)
        self.root = None
        self.logger.info("Tree created")

    def _is_empty(self) -> bool:
        """
        Checks for empty tree
        If root == None return True, else False
        """
        return not bool(self.root)

    def insert(self, data):
        """Adds element to the tree"""
        node = Node(data)
        if self._is_empty():
            self.logger.info("Tree is empty, adds %s to the root position", data)
            self.root = node
            return
        parent = self.root
        while parent:
            if node.data <= parent.data and parent.left:
                parent = parent.left
            elif node.data <= parent.data and not parent.left:
                self.logger.info("Find place for %s, left from %s", data, parent.data)
                parent.left = node
                return
            elif node.data > parent.data and parent.right:
                parent = parent.right
            elif node.data > parent.data and not parent.right:
                self.logger.info("Find place for %s, right from %s", data, parent.data)
                parent.right = node
                return

    def _lookup(self, data, node):
        """Look for data in tree"""
        if data == node.data:
            return node
        if data is None:
            return None
        if not node:
            return -1
        if data > node.data:
            return self._lookup(data, node.right)
        if data < node.data:
            return self._lookup(data, node.left)

    def lookup(self, data):
        """Public version of lookup"""
        if self._is_empty():
            self.logger.info("Tree is empty")
            return -1
        return self._lookup(data, self.root)

    def delete(self, data):
        """Delete node from tree"""
        if not self.lookup(data):
            raise DeleteError("Nothing to delete")
        node_to_delete = self.lookup(data)
        prev = None
        curr = self.root
        while True:  # looking for parent node
            if curr.data == data:
                break
            if data < curr.data:
                prev = curr
                curr = curr.left
            elif data > curr.data:
                prev = curr
                curr = curr.right

        # delete node without children
        if not node_to_delete.left and not node_to_delete.right:
            if not prev:
                self.root = None
            elif prev.left == node_to_delete:
                prev.left = None
            else:
                prev.right = None
        # delete node with right child
        if not node_to_delete.left and node_to_delete.right:
            if not prev:
                self.root = node_to_delete.right
            elif prev.left == node_to_delete:
                prev.left = node_to_delete.right
            else:
                prev.right = node_to_delete.right
        # delete with left child
        if node_to_delete.left and not node_to_delete.right:
            if not prev:
                self.root = node_to_delete.left
            elif prev.left == node_to_delete:
                prev.left = node_to_delete.left
            else:
                prev.right = node_to_delete.left
        # delete node with both children
        if node_to_delete.left and node_to_delete.right:
            left_rightest_child = node_to_delete.left
            while left_rightest_child.right:
                left_rightest_child = left_rightest_child.right
            if not prev:
                self.root = left_rightest_child
                self.root.left = node_to_delete.left
                self.root.right = node_to_delete.right
                return
            if prev.left == node_to_delete:
                prev.left = left_rightest_child
                self.logger.info("parent left %s", left_rightest_child.data)
                left_rightest_child.right = node_to_delete.right
                self.root.left = node_to_delete.left
                return
            else:
                prev.right = left_rightest_child
                left_rightest_child.right = node_to_delete.right
                self.root.left = node_to_delete.left


class Vertex:
    """
    Class implements vertex of the graph

    Attributes
    ----------
    name: str
        name of a vertex
    edges: LinkedList
        list of pointers on edges of current vertex
    """

    def __init__(self, name: str):
        self.name = name
        self.edges = LinkedList()

    def __eq__(self, other):
        return self.name == other

    def get_name(self):
        """Return vertex name"""
        return self.name


class Graph:
    """
    Class implements a graph structure

    Methods
    -------
    insert(vertex, edge):
        adds a vertex to the graph and edges for current vertexes

    lookup(name): Vertex
        Returns a pointer on a vertex with name is equals name argument

    delete(name):
        Deletes a vertex with name equals name argument

    Attributes
    ---------
    vertices: LinkedList
        The list of vertices belongings to graph
    count: int
        Count of vertices in graph

    """
    logger = logging.getLogger("Graph")
    c_handler = logging.StreamHandler(stream=sys.stdout)
    c_formatter = logging.Formatter("%(name)s - %(message)s ")
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(logging.INFO)
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    def __init__(self):
        self.vertices = LinkedList()
        self.count = 0
        log = logging.getLogger("Tree")
        log.setLevel(logging.WARNING)
        logger = logging.getLogger("Linked list")
        logger.setLevel(logging.WARNING)
        logger.info("Graph created")

    def _get_count(self) -> int:
        """Returns count of vertices"""
        return self.count

    def _is_empty(self) -> bool:
        """Returns Ture if graph has vertices else - False"""
        return not bool(self.vertices)

    def insert(self, vertex: str, *edges: 'names of vertices should be linked'):
        """
        Method adds vertex to the graph and create edges.
        If tries to create edge to unexisting vertex raises EdgeException
        """
        if self._is_empty() and len(edges) > 0:
            raise EdgeError("Can`t add edges in empty graph")
        vert = Vertex(vertex)
        if self.vertices.lookup(vert) > -1:
            self.logger.info("Vertex %s already in the graph", vert.name)
            return
        self.logger.info(">>>Adds vertex %s", vertex)
        if edges:
            for edge in edges:
                edge = Vertex(edge)
                req_vertex = self.vertices.lookup(edge)
                req_vertex = self.vertices.value(req_vertex)
                if not req_vertex:
                    raise EdgeError(f"Can't connect{vertex} to {edge},"
                                    f"{edge} doesnt exist")
                vert.edges.append(req_vertex)
                self.logger.info("Adds edge %s %s", vert.name, req_vertex.name)
                req_vertex.edges.append(vert)
        self.vertices.append(vert)
        self.count += 1

    def print_graph(self):
        """Prints graph"""
        vert = self.vertices.head
        while vert:
            print(vert.data.name, "|->", end=" ")
            edge = vert.data.edges.head
            while edge:
                print(edge.data.name, "-->", end=" ")
                edge = edge.next
            print("|\n")
            vert = vert.next

    def lookup(self, vertex: str):
        """
        Looks for vertex
        If it founds returns pointer
        Else returns None

        """
        vert = self.vertices.head
        count = 0
        while vert:
            if vert.data.name == vertex:
                self.logger.info("Position of %s is %s", vertex, count)
                return vert
            count += 1
            vert = vert.next
        return None

    def delete(self, vertex: LLNode):
        """Deletes vertex and edges"""
        ind = self.vertices.lookup(vertex.data)
        self.vertices.delete(ind)
        edge = vertex.data.edges.head
        while edge:
            curr_ind = edge.data.edges.lookup(vertex.data)
            try:
                if curr_ind >= 0:
                    edge.data.edges.delete(curr_ind)
            finally:
                edge = edge.next


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.append(10)
    l_list.append(23)
    l_list.prepend(5)
    l_list.insert("ss", 1)
    l_list.lookup(10)
    l_list.print_list()
    l_list.delete(2)
    l_list.print_list()

    print(">>>>>>>>>>")
    my_queue = Queue()
    my_queue.enqueue(44)
    my_queue.enqueue(55)
    print(my_queue.peek())
    my_queue.dequeue()
    my_queue.dequeue()
    print(">>>>>>>>>>")
    my_stack = Stack()
    my_stack.push("a")
    my_stack.push("b")
    my_stack.pop()
    print(my_stack.peek())

    my_hash = HashTable()
    my_hash.insert("abc", "zz")
    my_hash.insert(1, 2)
    my_hash.insert(1, 10)
    my_hash.delete(1)
    print(f"Position of 1 {my_hash.lookup(1)}")
    11, 9, 20, 7, 10, 19, 21
    my_tree = BST()
    my_tree.insert(18)
    my_tree.insert(10)
    my_tree.insert(25)
    my_tree.insert(7)
    my_tree.insert(15)
    my_tree.delete(10)
    print(my_tree.lookup(7))
    print(">>>>>>>>>>")
    g = Graph()
    g.insert("A")
    g.insert("B", "A")
    g.insert("C", "A", "B")
    g.insert("A")
    g.lookup("B")

    g.print_graph()

    g.delete(g.lookup("A"))
    g.print_graph()
