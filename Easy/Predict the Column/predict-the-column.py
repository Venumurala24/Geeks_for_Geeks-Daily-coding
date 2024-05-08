#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        
        max=0
        d=0
        flag=False
        
        for i in range(N):
            c=0
            for j in range(N):
                if arr[j][i]==0:
                    c+=1
                    if c>max:
                        max=c
                        d=i
                        flag=True
            
        if flag:
            return d
        else:
            return ("-1")
        # return d
                    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends