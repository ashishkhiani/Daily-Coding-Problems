## Problem 

Given the mapping `a = 1, b = 2, ... z = 26`, and an encoded message, count the number of ways it can be decoded.
For example, the message `111` would give 3, since it could be decoded as `aaa`, `ka`, and `ak`.
You can assume that the messages are decodable. For example, `001` is not allowed.

## Solution

The solution derived here has a time complexity of `O(n^2)` where `n` is the length of the message.

Given an encoded message `M` of size `n`, we need to determine the list of possible ways it can be decoded. 
We will utilize a dynamic programming approach to solve this problem, that is, we will break the problem into smaller sub-problems and solve.
The idea is to decode sub-messages of `M` in hopes of finding all the possible decodings of `M`.

As an example, consider the message `M = 17124`, we can divide the message into sub-messages as follow, 
(`M[i:j]` represents the string of characters from position `i` (included) to `j` (excluded)):

| sub-messages |          |
|--------------|----------|
| ''           | `M[0:0]` |
| 1            | `M[0:1]` |
| 17           | `M[0:2]` |
| 171          | `M[0:3]` |
| 1712         | `M[0:4]` |
| 17124        | `M[0:5]` |

Generally speaking, any message `M` of size `n` can be divided following this same approach: 
`m_0 = M[0:0], m_1 = M[0:1], m_2 = M[0:2], ..., m_i = M[0:i], ..., m_n = M[0:n]`.

Now that we have an idea of how to split the problem into smaller sub-problems, we can describe the algorithm: 

1. Construct a dictionary of key-value pairs such that the key is a sub-message and the value is an empty list representing possible decodings.
   For example, the dictionary for the message M = 17124 can be initialized as: 

    | sub-messages | possible decodings |
    |--------------|--------------------|
    | ''           | `[]`               |
    | 1            | `[]`               |
    | 17           | `[]`               |
    | 171          | `[]`               |
    | 1712         | `[]`               |
    | 17124        | `[]`               |

2. For each sub-message in the dictionary (ascending order):
    1. Split it such that the left hand side (LHS) of the sub-message is a key in the dictionary. Each of these will be referred to as tuples.
    2. For each of the tuples created, if the right hand side (RHS) of the message is a key in the mapping, 
       then concatenate all the possible mappings of the LHS with the mapping of the RHS. 
       
The idea of this algorithm is to use the decodings of the sub-messages to find the decoding of the original message.

The table below shows the algorithm in action. 
The possible tuples is a list of all the message fragments generated when performing step 2.1 of the algorithm.
The valid tuples is a list of all the message fragments where the RHS is a key in the mapping. 


|iteration  | sub-messages | possible tuples                                          | valid tuples           | possible encodings                   |
|-----------|--------------|----------------------------------------------------------|------------------------|--------------------------------------|
| 1         | ''           | -                                                        | -                      | `''`                                 |
| 2         | 1            | `('', 1)`                                                | `('', 1)`              | `a`                                  |
| 3         | 17           | `(1, 7), ('', 17)`                                       | `(1, 7), ('', 17)`     | `ag, q`                              |
| 4         | 171          | `(17, 1), (1, 71), ('', 171)`                            | `(17, 1)`              | `aga, qa`                            | 
| 5         | 1712         | `(171, 2), (17, 12), (1, 712), ('', 1712)`               | `(171, 2), (17, 12)`   | `agab, qab, agl, ql`                 |
| 6         | 17124        | `(1712, 4), (171, 24), (17, 124), (1, 7124), ('', 7124)` | `(1712, 4), (171, 24)` | `agabd, qabd, agld, qld, agax, qax`  |
