#User function Template for python3
import math
class Solution:
    def jugglerSequence(self, n):
        # code here
        
        a = n 
      
        # print the first term 
        print (a,end=" ") 
          
        # calculate terms until last term is not 1 
        while (a != 1) : 
            b = 0
              
            # Check if previous term is even or odd 
            if (a%2 == 0) : 
                  
                # calculate next term 
                b  = (int)(math.floor(math.sqrt(a))) 
       
            else : 
                # for odd previous term calculate 
                # next term 
                b = (int) (math.floor(math.sqrt(a)*math.sqrt(a)*
                                             math.sqrt(a))) 
       
            print (b,end=" ") 
            a = b 
        
        
        return ''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends