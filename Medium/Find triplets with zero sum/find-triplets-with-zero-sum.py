#Back-end complete function Template for Python 3

class Solution:
    #Function to find triplets with zero sum.
    def findTriplets(self, a, n):
        
        #Sorting the elements.
        a.sort()
        
        #Traversing the array elements.
        for i in range(n-2):
            
            #Taking two pointers. One at element after ith index and another
            #at the last index.
            l=i+1
            r=n-1
            
            #Using two pointers over the array which helps in checking if
            #the triplet sum is zero.
            while(l<r):
                curr_sum=a[i]+a[l]+a[r]
                
                #If sum of elements at indexes i, l and r is 0, we return true.
                if(curr_sum==0):
                    return 1
                #Else if the sum is less than 0, it means we need to increase the
                #sum so we increase the left pointer l.
                elif(curr_sum<0):
                    l+=1
                #Else the sum is more than 0 and we need to decrease the
                #sum so we decrease the right pointer r.
                else:
                    r-=1
                    
         #returning false if no triplet with zero sum is present.           
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends