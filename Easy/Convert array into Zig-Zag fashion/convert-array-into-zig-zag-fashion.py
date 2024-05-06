#User function Template for python3


class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        
        
        flag=True
        i=0
        while i<n-1:
            if arr[i]>arr[i+1] and flag==True:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=False
                
                
            elif arr[i]<arr[i+1]  and flag==False:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=True
            
            elif arr[i]<arr[i+1] and flag==True:
                flag=False
            
            else:
                if arr[i]>arr[i+1] and flag==False:
                    flag=True
                
            i+=1


        
        
        # 4,3,7,8,6,2,1
       
        # 3,4,7,8,6,2,1
        
        # 3,7,4,8,6,2,1
        
        # 3,7,4,8,6,2,1
        
        # 3,7,4,8,2,6,1
            
      
            

# 1
# 9825  
#                 # [3, 7, 4, 8, 2, 6, 1]
            
            
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys


def isZigzag(arr, n):
    f = 1

    for i in range(1, n):
        if f:
            if arr[i-1] > arr[i]:
                return 0
        else:
            if arr[i-1] < arr[i]:
                return 0
        f = f ^ 1

    return 1

t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.zigZag(arr, n)
    check = isZigzag(arr, n)

    if check:
        print("1")
    else:
        print("0")

    t -= 1

sys.exit(0)

# } Driver Code Ends