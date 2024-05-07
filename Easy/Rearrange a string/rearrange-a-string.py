#User function Template for python3

class Solution:
    def arrangeString(self, s):
        
        c=[]
        max=0
        for i in s:
            if i.isalpha():
                c.append(i)
        
        
        d=0
        for i in s:
            if i.isdigit():
                d+=int(i)
        
        if d==0:
            c=sorted(c)
            return ''.join(c)
        
        
        c=sorted(c)
        c.extend(str(d))
        
        return ''.join(c)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends