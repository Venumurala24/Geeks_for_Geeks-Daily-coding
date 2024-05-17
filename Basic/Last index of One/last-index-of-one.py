#User function Template for python3

class Solution:
    def lastIndex(self, s):
        c=0
        f=False
        
        for i in range(len(s)):
            if s[i]=='1':
                c=i
                f=True
            
            
        if f==False:
            return ('-1')
        
        return c
            
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends