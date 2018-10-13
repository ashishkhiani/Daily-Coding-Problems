from collections import deque


def split_stack(stack, queue):
    half = len(stack) / 2
    while len(stack) > half:
        temp = stack.pop()
        queue.append(temp)


def interleave_helper(stack, queue):
    if stack:
        temp = stack.pop()
        interleave_helper(stack, queue)
        stack.append(temp)
        stack.append(queue.popleft())


def interleave(stack):
    if not stack:
        return []

    queue = deque([])
    split_stack(stack, queue)
    interleave_helper(stack, queue)
    if queue:
        stack.append(queue.popleft())

    return stack

