def calculate_h_index(_input):
    h_index = 0
    _input.sort()

    for i, current in enumerate(_input):

        remaining_elements = len(_input) - i

        if remaining_elements >= current:
            h_index = current

    return h_index
