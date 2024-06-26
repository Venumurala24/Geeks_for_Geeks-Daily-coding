#Back-end complete function Template for Python 3

class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        flag = True
        for i in range(n - 1):
            # swapping elements if flag is True and current element is greater than next element
            if flag:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # swapping elements if flag is False and current element is smaller than next element
            else:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = not flag


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys


def isZigzag(arr, n):
    f = 1

    for i in range(1, n):
        if f:
            if arr[i-1] > arr[i]:
                return 0
        else:
            if arr[i-1] < arr[i]:
                return 0
        f = f ^ 1

    return 1

t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.zigZag(arr, n)
    check = isZigzag(arr, n)

    if check:
        print("1")
    else:
        print("0")

    t -= 1

sys.exit(0)

# } Driver Code Ends