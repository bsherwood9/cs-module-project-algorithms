'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# O(n^2)


def single_number(arr):
    # Your code here
    # want to go through the list if the item exist
    # could have done this with a set.
    copy = []
    for i in arr:
        if i not in copy:
            copy.append(i)
        else:
            copy.remove(i)
    return copy[0]
    # put it an a different array
    # return int

    # O(n)
    # use a set when you need the uniqueness property
    #s = set()
    # for num in arr:
    #         if num in s:
    #             s.remove(num)
    #         else:
    #             s.add(num)
    # return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
