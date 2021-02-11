class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val}, {self.left}, {self.right})'


def serialize_recursively(root, result):
    """
    We serialize the tree recursively by iterating the binary tree in a pre-orderly fashion.
    This algorithm visits each node once hence it has a time complexity of O(n)
    Recursion might lead to stack overflow errors if the tree is large enough
    """
    if root is None:
        return result + '()'

    result = root.val + serialize_recursively(root.left, result) + serialize_recursively(root.right, result)
    return '(' + result + ')'


def serialize(root):
    return serialize_recursively(root, '')


def find_index_of_closing_bracket(string, index_open):
    stack = []

    for i in range(index_open, len(string)):
        char = string[i]

        if char == '(':
            stack.append(char)

        elif char == ')':
            if stack[-1] == '(':
                stack.pop()

        if len(stack) == 0:
            return i

    return -1


def deserialize_recursively(string):
    """
    The way we serialized the string makes deserializing inefficient.
    This is because we need to parse the string every time to find the left hand side (lhs) and right hand side (rhs)
    # TODO find a better way to serialize and deserialize the string
    """
    if string == '()':
        return None

    string = string[1:-1]  # strip first and last parenthesis

    index_open = string.find('(')  # index of first '('
    val = string[:index_open]

    index_close = find_index_of_closing_bracket(string, index_open) + 1
    lhs = string[index_open:index_close]
    rhs = string[index_close:]

    return Node(val, deserialize_recursively(lhs), deserialize_recursively(rhs))


def deserialize(string):
    return deserialize_recursively(string)
