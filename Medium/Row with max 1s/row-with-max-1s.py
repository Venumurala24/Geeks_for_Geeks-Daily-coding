#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    max=0
	    c=0
	    k=0
	    flag=False
		for i in range(n):
		    c=0
		    for j in range(m):
		        if arr[i][j]==1:
		            c+=1
		            flag=True
            if c>max:
                max=c
                k=i
		
		
	    if flag:
	        return k
	   
	    return ("-1")
		                
	
		            
		            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends