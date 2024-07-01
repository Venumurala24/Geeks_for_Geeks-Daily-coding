class Solution:
    def nthFibonacci(self, n : int) -> int:
        mod = 10**9 + 7

        #initialize the dp array with 0 and 1 for base cases
        dp = [0] * (n + 5)
        dp[0] = 0
        dp[1] = 1

        #compute the fibonacci numbers using dynamic programming
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] % mod + dp[i - 2] % mod) % mod
        
        #return the nth fibonacci number
        return dp[n]


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends