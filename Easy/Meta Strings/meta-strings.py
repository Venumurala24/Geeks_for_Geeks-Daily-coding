#User function Template for python3
class Solution:
    def metaStrings(self, s1, s2):
        
        if s1==s2:
            return False
        
        c=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
        if sorted(s1) == sorted(s2):
            if c==2 :
                return True
        return False
        

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        obj = Solution()
        if obj.metaStrings(S1, S2):
            print(1)
        else:
            print(0)
# } Driver Code Ends