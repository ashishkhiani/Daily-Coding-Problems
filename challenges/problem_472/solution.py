from challenges.problem_472.mapping import mapping


def decode_message(message):
    table, n = {'': ['']}, len(message) + 1

    for i in range(1, n):
        sub_message = message[0:i]
        table[sub_message] = []
        _decode_sub_message(sub_message, table)

    return table[message]


def _decode_sub_message(message, table):
    for i in reversed(range(len(message))):
        lhs, rhs = message[:i], message[i:]

        if rhs in mapping:
            table[message] += list(map(lambda x: x + mapping[rhs], table[lhs]))
