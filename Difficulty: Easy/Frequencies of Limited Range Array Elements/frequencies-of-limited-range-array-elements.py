class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        
        
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        # print(d)    
        
        for i in range(1,N+1):
            
            if i not in d:
                arr[i-1]=0
            elif i in d:
                arr[i-1]=d[i]
            
                
            
            
        # for i in range(1,N):
        #     if i in arr:
        #         c[i]=arr.count(i)
        #     else:
        #         c[i]=0
        
        
        # for i in range(N):
        #     arr[i]=c[i]
        
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends