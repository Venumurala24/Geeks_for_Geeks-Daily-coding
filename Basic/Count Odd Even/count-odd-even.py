#User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
		c=0
		d=0
		for i in arr:
		    if i%2 ==0:
		        c+=1
		    else:
		        d+=1
		
		return (d,c)


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):
        n = int(input())

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr, n)

        # Printing the result
        print(*res)

# } Driver Code Ends