#User function Template for python3
class Solution:
	def isPanagram(self, S):
	    a=[]
        for i in range(len(S)):
            if S[i]!=' ' and S[i].isalpha():
                    a.append(S[i].lower())
        
        if len(set(a)) ==26:
            return '1'
        else:
            return '0'
            
        
    
# 		a={}
# 		for i in range(len(S)):
# 		    if S[i]!=' ' and S[i].isalpha():
# 		        a[S[i]]=1
# 		c=0        
# 		for i,v in a.items():
# 		    if a[i]==1:
# 		        c+=1
		
# 		if c == 26:
# 		    return '1'
# 		else:
# 		    return '0'
		        
		 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends