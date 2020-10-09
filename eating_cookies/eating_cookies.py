'''
Input: an integer
Returns: an integer
'''

# O(3^n)


# def eating_cookies(n):
#     #     # options = [3, 2, 1]
#     #     # count = 0
#     #     # if n == 0:
#     #     #     return count++
#     #     # what is the base case?
#     if n < 0:
#         return 0
#     # if n = 0, it represents there being a number of cookies where we can just take
#     # that many cookies
#     if n == 0:
#         return 1
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
