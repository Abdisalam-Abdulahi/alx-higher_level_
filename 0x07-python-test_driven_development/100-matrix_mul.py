#!/usr/bin/python3
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    m_b_col = []
    new_lis = []
    sub_arr = []
    sum = 0

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for sub_list in m_a:
        if type(sub_list) is not list:
            raise TypeError("m_a must be a list of lists")

    for sub_list in m_b:
        if type(sub_list) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a) - 1):
        if len(m_a[i]) != len(m_a[i + 1]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(len(m_b) - 1):
        if len(m_b[i]) != len(m_b[i + 1]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_b) - 1):
        for k in range(len(m_b[i])):
            m_b_col.append([m_b[i][k], m_b[i + 1][k]])
    # print(m_b_row)
    for li in m_a:
        for i in range(len(m_b)):
            for k in range(len(m_b[i])):

                if type(li[k]) is not int and type(li[k]) is not float:
                    raise TypeError("m_a should contain only"
                                    " integers or floats")

                if type(m_b_col[i][k]) is not int \
                        and type(m_b_col[i][k]) is not float:
                    raise TypeError("m_b should contain"
                                    " only integers or floats")
                sum += li[k] * m_b_col[i][k]
            sub_arr.append(sum)
            sum = 0
        new_lis.append(sub_arr)
        sub_arr = []
    return (new_lis)
