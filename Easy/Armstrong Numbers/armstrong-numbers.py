#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        s = n  # assigning input value to the s variable
        b = len(str(n))
        sum1 = 0
        while n != 0:
            r = n % 10
            sum1 = sum1+(r**b)
            n = n//10
        if s == sum1:
            return "Yes"
        else:
            return  "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends