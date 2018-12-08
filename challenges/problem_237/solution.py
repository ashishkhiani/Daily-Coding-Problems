from challenges.problem_237.Node import Node


def is_symmetric(node):
    """
    :type node: Node
    """
    if node is None:
        return

    stack = [node]
    stack_complement = [node]

    while len(stack) > 0:

        x = stack.pop()
        x_complement = stack_complement.pop()

        if x.name() == x_complement.name():

            for child in reversed(x.children()):
                stack.append(child)

            for child in x_complement.children():
                stack_complement.append(child)

        else:
            return False

    return True
