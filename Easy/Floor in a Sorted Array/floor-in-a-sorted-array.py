class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        c=0
        d=0
        k=True
        for i in range(N):
            if A[i]<=X and A[i]>c:
                c=A[i]
                d=i
                k=False
        if k:
            return ('-1')
        else:
            return d
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends