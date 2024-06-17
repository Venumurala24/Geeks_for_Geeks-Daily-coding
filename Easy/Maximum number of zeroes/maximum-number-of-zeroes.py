# User Template code

def MaxZero(arr, n):
    # Your code goes here
    arr.sort(reverse=True)
    res=out=-1
    for i in arr:
        ans = str(i).count('0')
        if ans > res and ans != 0:
            res=ans
            out=i
    return out        








#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        print(MaxZero(a,n))
# } Driver Code Ends