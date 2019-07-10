# // integer divsion
# divmod(x, y) Return (x // y, x % y) as tuple, if x and y are integers.

# We use the tuple, (ValueError, EOFError), to designate the types of errors that we
# # wish to catch with the except-clause. In this implementation, we catch either error

# [ k k for k in range(1, n+1) ] list comprehension
# { k k for k in range(1, n+1) } set comprehension
# ( k k for k in range(1, n+1) ) generator comprehension
# { k : k k for k in range(1, n+1) } dictionary comprehension
# The generator syntax is particularly attractive when results do not need to be stored
# in memory. For example, to compute the sum of the first n squares, the generator
# syntax, total = sum(k k for k in range(1, n+1)), is preferred to the use of an
# explicitly instantiated list comprehension as the parameter.

# When using a simultaneous assignment, all of the expressions are evaluated
# on the right-hand side before any of the assignments are made to the left-hand
# variables. This is significant, as it provides a convenient means for swapping the
# values associated with two variables:
# j, k = k, j
# With this command, j will be assigned to the old value of k, and k will be assigned
# to the old value of j. Without simultaneous assignment, a swap typically requires
# more delicate use of a temporary variable, such as
# temp = j
# j = k
# k = temp

def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]

def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]

# def solutionTJ(M, A):
#     N = len(A)
#     count = [0] * (M + 1)
#     maxOccurence = 1
#     index = -1
#     for i in range(N):
#         if count[A[i]] > 0:
#             # tmp = count[A[i]]
#             if count[A[i]] > maxOccurence:
#                 maxOccurence = count[A[i]]
#                 index = i
#             count[A[i]] += 1
#         else:
#             count[A[i]] = 1
#     return A[index]

print(solution(3,[2,2,1,3]))
# print(solution(3,[1,2,3,3,1,3,1]))
# print(solution(3,[1]))