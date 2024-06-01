
class Solution:
    def oddEven(self, S : str) -> str:
        from collections import Counter
    
    # Get the frequency of each character in the string
        frequency = Counter(s)
        
        x = 0
        y = 0
        
        # Iterate over the frequency dictionary
        for char, freq in frequency.items():
            # Calculate the position of the character in the English alphabet (1-based index)
            position = ord(char) - ord('a') + 1
            
            if position % 2 == 0 and freq % 2 == 0:
                x += 1
            elif position % 2 != 0 and freq % 2 != 0:
                y += 1
        
        # Calculate the sum of x and y
        result = x + y
        
        # Return "EVEN" or "ODD" based on the result
        return "EVEN" if result % 2 == 0 else "ODD"

                


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends