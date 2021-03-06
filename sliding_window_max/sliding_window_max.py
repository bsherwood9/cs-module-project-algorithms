'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # we need to loop through every item
    count = 0
    answer = []
    for i in range(len(nums)-k+1):
        answer.append(max(nums[count:k]))
        count += 1
        k += 1
    return answer
    # we need to increment our window every time we loop.
    # then take the max from every window
    # append the max to a new arr
    # return the array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
