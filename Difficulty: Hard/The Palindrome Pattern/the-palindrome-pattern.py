class Solution:

    def pattern(self, arr):
        n = len(arr)
        temp = [0] * n
        flag = 0
        ans = ""

        for i in range(n):
            for j in range(n):
                temp[j] = arr[i][
                    j]  # Copying each row of the 2D array to a temporary array.

            if self.is_palindrome(
                    temp):  # Checking if the row is a palindrome.
                flag = 1
                ans = str(
                    i
                ) + " " + "R"  # Setting the answer as the row index and "R" to indicate the pattern is in a row.
                break

        if flag == 0:
            for j in range(n):
                for i in range(n):
                    temp[i] = arr[i][
                        j]  # Copying each column of the 2D array to a temporary array.

                if self.is_palindrome(
                        temp):  # Checking if the column is a palindrome.
                    flag = 1
                    ans = str(
                        j
                    ) + " " + "C"  # Setting the answer as the column index and "C" to indicate the pattern is in a column.
                    break

        if flag == 0:
            ans = "-1"  # If no palindrome pattern is found, set answer as -1.

        return ans  # Return the answer.

    # Function to check if the given array is a palindrome.
    def is_palindrome(self, arr):
        n = len(arr)
        mid = n // 2

        for i in range(mid):
            if arr[i] != arr[n - 1 - i]:
                return False

        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends