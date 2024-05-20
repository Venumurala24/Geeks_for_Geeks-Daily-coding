#Back-end complete function Template for Python 3

class Solution:
        
    def printNos(self,N):
        if(N>0):#The loop runs till N>1
            self.printNos(N-1)#We keep on recursing till the end as we want to print from 1 to N
            print(N,end=" ")#When recursion is done then print N
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends