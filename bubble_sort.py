# pseudo code from Wikipedia
# procedure bubbleSort( A : list of sortable items )
#     n = length(A)
#     repeat
#         swapped = false
#         for i = 1 to n-1 inclusive do
#             /* if this pair is out of order */
#             if A[i-1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap( A[i-1], A[i] )
#                 swapped = true
#             end if
#         end for
#     until not swapped
# end procedure


def sort(a):
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if a[i - 1] > a[i]:
                a[i - 1], a[i], swapped = a[i], a[i - 1], True
