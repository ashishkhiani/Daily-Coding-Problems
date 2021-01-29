def get_product(num_list):
    product = 1

    for num in num_list:
        if num == 0:
            continue
        else:
            product = product * num

    return product


def problem_2_division_linear(num_list):
    """
    This solution uses division and has a time complexity of O(n)
    """
    if len(num_list) < 2:
        raise Exception("List must have more than one number")

    product = get_product(num_list)

    if 0 in num_list:
        return list(map(lambda num: 0 if num != 0 else product, num_list))
    else:
        return list(map(lambda num: product / num, num_list))


def problem_2_no_division_polynomial_slow(num_list):
    """
    This solution does not use division, but has a time complexity of O(n^2)
    """
    n = len(num_list)

    if n < 2:
        raise Exception("List must have more than one number")

    result = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= num_list[j]

        result.append(product)

    return result


def problem_2_no_division_polynomial_faster(num_list):
    """
    This solution does not use division, but has a time complexity of O(n^2)
    This solution however is faster than the previous polynomial solution
    """
    n = len(num_list)

    if n < 2:
        raise Exception("List must have more than one number")

    result = [num_list[1], num_list[0]]

    for i in range(2, n):
        temp = result[-1]
        result = list(map(lambda x: x * num_list[i], result))
        result.append(temp * num_list[i - 1])

    return result


def problem_2_no_division_linear(num_list):
    """
    This solution does not use division and has a time and space complexity of O(n)
    """
    n = len(num_list)

    if n < 2:
        raise Exception("List must have more than one number")

    result = []
    accumulator = 1  # nothing to the left of the first element, so we multiply by 1

    # calculate product of numbers to the left of num_list[i]
    for i in range(n):
        result.append(accumulator)
        accumulator *= num_list[i]

    accumulator = 1  # nothing to the right of the last element, so we multiply by 1

    # calculate product of numbers to the right of num_list[i], and then calculate the final product
    for i in range(n - 1, -1, -1):
        result[i] *= accumulator
        accumulator *= num_list[i]

    return result


def problem_2(num_list):
    return problem_2_no_division_linear(num_list)
