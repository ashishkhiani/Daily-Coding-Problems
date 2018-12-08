from challenges.problem_237.Node import Node


class Traversal(object):

    @staticmethod
    def left_preorder_traversal(node):
        """
        :type node: Node
        """
        print(node.name(), end=" ")
        for child in node.children():
            if child.is_leaf():
                print(child.name(), end=" ")
            else:
                Traversal.left_preorder_traversal(child)

    @staticmethod
    def right_preorder_traversal(node):
        """
        :type node: Node
        """
        print(node.name(), end=" ")
        for child in reversed(node.children()):
            if child.is_leaf():
                print(child.name(), end=" ")
            else:
                Traversal.right_preorder_traversal(child)