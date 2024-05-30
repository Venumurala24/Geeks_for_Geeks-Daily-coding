#Back-end complete function Template for Python 3

class Solution:
    
    #Function to rearrange the elements in the given array.
    def reArrange(self, arr, N):
        oddInd = 1
        evenInd = 0
        
        while (True): 
            
            #Finding the next even index.
            while (evenInd < N and arr[evenInd] % 2 == 0): 
                evenInd += 2
                  
            #Finding the next odd index.
            while (oddInd < N and arr[oddInd] % 2 == 1): 
                oddInd += 2
                   
            #Swapping the elements at even and odd indices.
            if (evenInd < N and oddInd < N): 
                    arr[evenInd],arr[oddInd] = arr[oddInd],arr[evenInd]
                
                   
            else: 
                break


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def check(arr, n):
    flag = 1
    c=d=0
    for i in range(n):
        if i%2==0:
            if arr[i]%2:
                flag = 0
                break
            else:
                c+=1
        else:
            if arr[i]%2==0:
                flag = 0
                break
            else:
                d+=1
    if c!=d:
        flag = 0
            
    return flag
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ob.reArrange(arr,N)
        
        print(check(arr,N))

# } Driver Code Ends