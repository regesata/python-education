"""
Module with tests for to_test module
uses pytests library
"""
import sys

import pytest
import data_structures as ds


@pytest.mark.parametrize("data, expected", [
    (1, 1),
    ("aa", "aa"),
    ([123, 123], [123, 123])
])
def test_llnode(data, expected):
    """Test case for LLNode.__init__()"""
    node = ds.LLNode(data)
    assert node.data == expected, "Should be 1"


@pytest.mark.parametrize("data, expected", [
    (1, 1),
    ("aa", "aa"),
    ("1asd23", "1asd23")
])
def test_node__str__(data, expected):
    """Test cases for LLNode.__str__()"""
    assert ds.LLNode(data).__str__() == f"Node: {expected}"


@pytest.mark.parametrize("data, expected", [
    (1, 1),
    ("aa", "aa"),
    ("1asd23", "1asd23")
])
def test_node__repr__(data, expected):
    """Test cases for LLNode.__str__()"""
    assert ds.LLNode(data).__repr__() == f"Node<data={expected}>"


def test_linked_list_init():
    """Test case for LList.__init__()"""
    l_list = ds.LinkedList()
    assert l_list.tail is None, "Should be None"
    assert l_list.head is None, "Should be None"


@pytest.mark.parametrize("data, expected", [
    (100, 100),
    ("list", "list"),
    ([11, 22, 33], [11, 22, 33]),
    (None, None)
])
def test_prepend_l_list(data, expected):
    """Test cases for LList.prepend()"""
    l_list = ds.LinkedList()
    l_list.prepend(data)
    assert l_list.head.data == expected
    l_list.prepend(data)
    assert l_list.head.data == expected


@pytest.mark.parametrize("data, expected", [
    (100, 100),
    ("list", "list"),
    ([11, 22, 33], [11, 22, 33]),
    (None, None)
])
def test_prepend_l_list(data, expected):
    """Test cases for LList.prepend()"""
    l_list = ds.LinkedList()
    l_list.append(data)
    assert l_list.tail.data == expected
    l_list.append(data)
    assert l_list.tail.data == expected


@pytest.mark.parametrize("nodes, find, expected", [
    ([1, 2, 3, 4], 3, 2),
    (["asd", "sec", "third"], "asd", 0),
    (["one", 4, "zero"], 3, -1)
])
def test_lookup(nodes, find, expected):
    """Test cases for LinkedList.lookup()"""
    l_list = ds.LinkedList()
    for node in nodes:
        l_list.append(node)
    assert l_list.lookup(find) == expected


@pytest.mark.parametrize("nodes, find, expected", [
    ([1, 2, 3, 4], 2, 3),
    (["asd", "sec", "third"], 0, "asd"),
    (["one", 4, "zero"], 3, None)
])
def test_value(nodes, find, expected):
    """Test cases for LilkedList.value()"""
    l_list = ds.LinkedList()
    for node in nodes:
        l_list.append(node)
    assert l_list.value(find) == expected


@pytest.mark.parametrize("nodes, index, data, expected", [
    ([1, 2, 3], 1, "zz", "zz"),
    (["asd", "sec", "third", "fourth"], 2, "zero", "zero"),
    (["one", 4, "zero"], 0, -1, -1)
])
def test_insert(nodes, index, data, expected):
    """Test cases for LinkedList.insert()"""
    l_list = ds.LinkedList()
    for node in nodes:
        l_list.append(node)
    l_list.insert(data, index)
    assert l_list.value(index) == expected


@pytest.mark.parametrize("nodes, index, expected", [
    ([1, 2, 3, 4], 0, 2),
    (["asd", "sec", "third"], 1, "third"),
    (["one", 4, "zero"], 2, None)
])
def test_delete(nodes, index, expected):
    """Test cases for LinkedList.delete()"""
    l_list = ds.LinkedList()
    for node in nodes:
        l_list.append(node)
    l_list.delete(index)
    assert l_list.value(index) == expected


@pytest.fixture
def redirected_output():
    """Fixture for LinkedList.print()"""
    l_list = ds.LinkedList()
    for char in "abc":
        l_list.append(char)


    class ListStream:
        """Class for redirecting print output"""
        def __init__(self):
            self.data = []

        def write(self, string):
            """Write to list"""
            self.data.append(string)

    sys.stdout = test = ListStream()
    l_list.print_list()
    yield " ".join(test.data)
    sys.stdout = sys.__stdout__


def test_print_list(redirected_output):
    """Test case for LList.print()"""
    assert redirected_output == "Head| a-->   b-->   c |Tail \n"


def test_queue_init():
    """Test case for Queue.__init__()"""
    t_queue = ds.Queue()
    assert t_queue._front is None, "Should be None"
    assert t_queue._rear is None, "Should be None"


@pytest.mark.parametrize("nodes, expected", [
    ([1, 2, 3, 4], 1),
    (["a", "b", "c"], "a")
])
def test_enqueue(nodes, expected):
    """Test cases for Queue.enqueue"""
    t_queue = ds.Queue()
    for node in nodes:
        t_queue.enqueue(node)
    assert t_queue._front.data == expected, f"Should be {expected}"


@pytest.mark.parametrize("nodes, expected", [
    ([1, 2, 3, 4], 1),
    (["a", "b", "c"], "a"),

])
def test_dequeue(nodes, expected):
    """Test cases for Queue.dequeue()"""
    t_queue = ds.Queue()
    for node in nodes:
        t_queue.enqueue(node)

    assert t_queue.dequeue().data == expected, f"Should be {expected}"


@pytest.mark.parametrize("nodes, expected", [
    ([1, 2, 3, 4], 2),
    (["a", "b", "c"], "b"),
    ([1], None),
    ([1, "a", 3], "a")
])
def test_peek(nodes, expected):
    """Tests cases for Queue.peek()"""
    t_queue = ds.Queue()
    for node in nodes:
        t_queue.enqueue(node)
    t_queue.dequeue()
    if t_queue.peek() is None:
        assert t_queue.peek() is None, f"Should be {expected}>"
    else:
        assert t_queue.peek().data == expected, f"Should be {expected}>"


def test_stack_init():
    """Test cases for Queue.__init__() """
    t_stack = ds.Stack()
    assert t_stack.top is None, "Should be None"
    assert isinstance(t_stack.list, ds.LinkedList), "Should be LinkedList"


@pytest.mark.parametrize("nodes, expected", [
    ([1], 1),
    (["a", "b"], "b")
])
def test_push(nodes, expected):
    """Test case for Stack.push()"""
    t_stack = ds.Stack()
    for node in nodes:
        t_stack.push(node)
    assert t_stack.list.tail.data == expected, f"Should be {expected}"


@pytest.mark.parametrize("nodes, expected, left", [
    ([1], 1, None),
    (["a", "b"], "b", "a")
])
def test_pop(nodes, expected, left):
    """Test cases for Stack.pop"""
    t_stack = ds.Stack()
    for node in nodes:
        t_stack.push(node)
    assert t_stack.pop().data == expected, f"Should be {expected}"
    if t_stack.top is None:
        assert t_stack.top is left, f"Should be {left}"
    else:
        assert t_stack.top.data == left, f"Should be {left}"


@pytest.mark.parametrize("nodes, expected", [
    ([1, 2, 3, 4], 4),
    (["a", "b", "c"], "c"),
    ([1], 1),
    ([1, "a", 3], 3)
])
def test_peek_stack(nodes, expected):
    """Test cases for Stack.peek()"""
    t_stack = ds.Stack()
    for node in nodes:
        t_stack.push(node)
    assert t_stack.peek().data == expected, f"Should be {expected}"


@pytest.mark.parametrize("key, value", [
    (1, 5),
    ("1", 5),
    ("a", 10),
    ("b", None)
])
def test_bucket_node_init(key, value):
    """Test case for BucketNode.__init__()"""
    t_node = ds.BucketNode(key, value)
    assert t_node.hash == hash(key), f"Should be {key}"
    assert t_node.value == value, f"Should be {value}"
    assert t_node.key == key, f"Should be {key}"


@pytest.mark.parametrize("key, value", [
    (1, 5),
    ("1", 5),
    ("a", 10),
    ("b", None)
])
def test_get_key_bucket_node(key, value):
    """Test case for Bucket_get_key"""
    t_node = ds.BucketNode(key, value)
    assert t_node.get_key() == key, f"Should be {key}"


@pytest.mark.parametrize("key, value", [
    (1, 5),
    ("1", 5),
    ("a", 10),
    ("b", None)
])
def test_get_value_bucket_node(key, value):
    """Test case for BucketNode_get_value"""
    t_node = ds.BucketNode(key, value)
    assert t_node.get_value() == value, f"Should be {value}"


def test_hash_table_init():
    """Test case for HashTable.__init__()"""
    t_table = ds.HashTable()
    assert isinstance(t_table.buckets, ds.LinkedList)


@pytest.mark.parametrize("nodes, expected", [
    ([(1, 1), (1, "a"), (1, 1)], 1),
    ([("a", 1), ("b", 2), ("c", 3)], 3)
])
def test_insert_hash_table(nodes, expected):
    """Test cases for NashTable.insert()"""
    t_table = ds.HashTable()
    for node in nodes:
        t_table.insert(*node)
    assert t_table.buckets.tail.data.value == expected, f"Should be {expected}"


@pytest.mark.parametrize("nodes, key, expected", [
    ([(1, 1), (2, "a"), (3, 1)], 1, "a"),
    ([("b", 2), ("c", 3)], "b", 3)
])
def test_delete_hash_table(nodes, key, expected):
    """Test cases for NashTable.delete()"""
    t_table = ds.HashTable()
    for node in nodes:
        t_table.insert(*node)
    t_table.delete(key)
    assert t_table.buckets.head.data.value == expected, f"Should be {expected}"


def test_node_init():
    """Test case for Node.__init__()"""
    t_node = ds.Node(1)
    assert t_node.left is None, "Should be None"
    assert t_node.right is None, "Should be None"


@pytest.mark.parametrize("data", [
    ("asd"),
    (123.3),
    ([1, 2, 3])
])
def test_node_init_exception(data):
    """Test cases raises ValueError"""
    with pytest.raises(ValueError) as error:
        ds.Node(data)
    assert error.type == ValueError



def test_bts_insert():
    """Test cases for BTS.insert()"""
    t_tree = ds.BST()
    t_tree.insert(12)
    assert t_tree.root.data == 12, "Should be 12"
    t_tree.insert(10)
    assert t_tree.root.left.data == 10, "Should be 10"
    t_tree.insert(22)
    assert t_tree.root.right.data == 22, "Should be 22"


@pytest.mark.parametrize("data, expected, left, right", [
    ([11, 9, 20, 7, 10, 19, 21], 11, 9, 20),
    ([18, 10, 25, 7, 15], 10, 7, 15),
])
def test_lookup_bts(data, expected, left, right):
    """Test cases for BTS.lookup()"""
    t_tree = ds.BST()
    for node in data:
        t_tree.insert(node)
    node = t_tree.lookup(expected)
    assert node.data == expected, f"Should be {expected}"
    assert node.left.data == left, f"Should be {left}"
    assert  node.right.data == right, f"Should be {right}"


@pytest.mark.parametrize("data, del_node, expected, left, right", [
    ([11, 9, 20, 7, 10, 19, 21], 11, 10, 9, 20),
    ([18, 10, 25, 7, 15], 15, None, None, None),
    ([18, 10, 25, 7, 15], 10, 7, None, 15)

])
def test_delete_bts(data, del_node, expected, left, right):
    """Test cases for BTS.delete()"""
    t_tree = ds.BST()
    for node in data:
        t_tree.insert(node)
    t_tree.delete(del_node)
    node = t_tree.lookup(expected)
    if node is None:
        assert node is None
        return

    assert node.data == expected, f"Should be {expected}"
    if node and (node.left is None):
        assert node.left is None
    else:
        assert node.left.data == left
    if node and (node.right is None):
        assert node.right is None
    else:
        assert node.right.data == right


def test_insert_graph():
    """Test cases for Graph.insert()"""
    t_graph = ds.Graph()
    t_graph.insert("A")
    t_graph.insert("B")
    t_graph.insert("C", "A", "B")
    assert t_graph.vertices.head.data.name == "A" # first vertex is A
    assert t_graph.vertices.head.data.edges.head.data.name == "C" # first edge of A is C
    assert t_graph.vertices.tail.data.edges.tail.data.name == "B" # last edge of C is B
    assert t_graph.vertices.head.next.data.edges.tail.data.name == "C" # first edge of B is C


def test_lookup_graph():
    """Test case for Graph.lookup()"""
    t_graph = ds.Graph()
    t_graph.insert("A")
    t_graph.insert("B")
    t_graph.insert("C", "A", "B")
    vert = t_graph.lookup("C")
    assert vert.data.name == "C"
    assert vert.data.edges.head.data.name == "A"
    assert vert.data.edges.tail.data.name == "B"


def test_delete_graph():
    """Test case for Graph.delete()"""
    t_graph = ds.Graph()
    t_graph.insert("A")
    t_graph.insert("B")
    t_graph.insert("C", "A", "B")
    t_graph.insert("D", "A", "B")
    t_graph.insert("E", "A", "B", "C", "D")
    vert = t_graph.lookup("E")
    assert vert.data.name == "E"
    edge = vert.data.edges.head
    edge_list = ["A", "B", "C", "D"]
    count = 0
    while edge:
        assert edge.data.name == edge_list[count]
        count += 1
        edge = edge.next
    t_graph.delete(t_graph.lookup("E"))
    vert = t_graph.vertices.head
    while vert:
        edge = vert.data.edges.head
        while edge:
            assert edge.data.name != "E"
            edge = edge.next
        vert = vert.next
