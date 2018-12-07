from challenges.problem_237.Node import Node
from challenges.problem_237.Traversal import Traversal

if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    i = Node("I")

    f.set_children([b, g])
    b.set_children([a, d])
    g.set_children([i])
    d.set_children([c, e])
    i.set_children([h])

    Traversal.left_preorder_traversal(f)
    print()
    Traversal.right_preorder_traversal(f)