#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        return ((n & 0x0f) << 4 | (n & 0xf0) >> 4)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends