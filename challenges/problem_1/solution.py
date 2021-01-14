from challenges.config import time_complexity, POLYNOMIAL, LINEAR


def problem1_polynomial(num_list, k):
    """This solution has a time complexity of O(n^2)"""
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == k:
                return True

    return False


def problem1_linear(num_list, k):
    """This solution has a time complexity of O(n) and space complexity of O(n)"""
    dictionary = {}

    for num in num_list:
        if num in dictionary:
            return True
        else:
            dictionary[k - num] = None

    return False


def problem_1(num_list, k):
    functions = {
        POLYNOMIAL: problem1_polynomial,
        LINEAR: problem1_linear,
    }

    return functions[time_complexity](num_list, k)



