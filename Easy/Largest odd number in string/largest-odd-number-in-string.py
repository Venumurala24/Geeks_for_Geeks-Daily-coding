#Back-end complete function Template for Python 3

class Solution:
    #Function to find the rightmost odd digit in the string.
    def maxOdd(self, s):
        p = -1
        #iterating over the string from the rightmost digit.
        for i in range(len(s)-1, -1, -1):
            #if the current digit is odd, store its index and break the loop.
            if int(s[i])&1:
                p = i
                break
        #if no odd digit is found, return an empty string.
        if p == -1:
            return ''
        #return the string from start till the rightmost odd digit index.
        return s[:p+1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxOdd(s))
# } Driver Code Ends