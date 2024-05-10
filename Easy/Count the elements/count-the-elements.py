#User function Template for python3
class Solution:
    
    #import math
    
   
        
    def countElements(self, a, b, n, query, q):
        
        b_ele_to_count = {} #defaultdict(int)
        b_max = 0
        for ele in b:
            if ele in b_ele_to_count:
                b_ele_to_count[ele] += 1
            else:
                b_ele_to_count[ele] = 1
            b_max = max(b_max, ele)
        
        
        a_max = 0
        for ele in a:
            a_max = max(a_max, ele)
        
        max_n = min(a_max,b_max)
        b_hist = [0]* (max_n+1)
        for i in range(0,max_n+1):
            if i > 0:
                b_hist[i] = b_hist[i-1] + b_ele_to_count.get(i,0)
            else:
                b_hist[i] = b_ele_to_count.get(i,0)
        
        #print(b, b_ele_to_count, b_hist)

        num_elements = [0]*q
        for i,a_index in enumerate(query):
            if a[a_index] > max_n:
                num_elements[i] =   b_hist[-1] 
            else:
                num_elements[i] = b_hist[a[a_index]]
        
        return num_elements
            
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends