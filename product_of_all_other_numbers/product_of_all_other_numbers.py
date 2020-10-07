'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # We look at all numbers and return product of all other numbers.
    # we should run the product function on every item in the list
    answer = []
    copy = arr[:]
    for c in arr:
        num = copy.pop(0)
        copy.append(num)
        count = 1
        for i in copy[:-1]:
            count *= i
        answer.append(count)
    return answer
    # we should append the item to the end of the list
    # run the product on every item but the last


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
