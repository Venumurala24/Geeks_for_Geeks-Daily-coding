#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):
    
    m = len(x)
    n = len(s)

    # A loop to slide pattern over text one by one
    for i in range(n - m + 1):
        # For current index i, check for pattern match
        j = 0
        while j < m and s[i + j] == x[j]:
            j += 1
        
        # If the entire pattern matches the text starting at index i
        if j == m:
            return i
        
    return("-1")

                
        

#{ 
 # Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends