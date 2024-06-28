class Solution:
    #Back-end complete function Template for Python 3

    #Function to find the leaders in the array.
    def leaders(self, n, arr):
        ans = []
        maxx = arr[n - 1]

        #We start traversing the array from last element.
        for i in range(n - 1, -1, -1):
            #Comparing the current element with the maximum element stored.
            #If current element is greater than max, we add the element.
            if arr[i] >= maxx:
                #Updating the maximum element.
                maxx = arr[i]
                #Appending the current element.
                ans.append(maxx)

        #Reversing the array.
        ans.reverse()
        #returning the answer.
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends