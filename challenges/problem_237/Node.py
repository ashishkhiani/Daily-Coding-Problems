import json
from typing import List


class Node(object):

    def __init__(self, name, children=None):
        """
        :type name: str
        :type children: List[Node]
        """
        if children is None:
            children = []
        self._name = name
        self._children = children

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

    def name(self):
        return self._name

    def children(self):
        return self._children

    def set_children(self, children):
        self._children = children

    def is_leaf(self):
        return not self._children

