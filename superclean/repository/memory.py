from entities import Node
from interfaces import INodeRepository


class NodeRepository(INodeRepository):
    _max_id = 0

    def __init__(self):
        root_node = Node(id=1, parent=None, value='root')
        self._nodes = [
            root_node,
            Node(id=2, parent=root_node, value="first level node 1"),
            Node(id=3, parent=root_node, value="first level node 2")
        ]
        self._max_id = 3

    def add_node(self, node):
        self._max_id += 1
        node.id = self._max_id
        self._nodes.append(node)
        return node

    def get_nodes(self, parent=None):
        res = []
        for node in self._nodes:
            if node.parent == parent:
                res.append(node)
        return res

    def start_transaction(self):
        pass

    def commit(self):
        pass
