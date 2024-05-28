#Back-end complete function Template for Python 3

#Function to find all the numbers with only 1,2 and 3 in their digits.
def findAll():
    num=1
    j=1
    
    #storing 1,2, and 3 in the list.
    a = [1, 2, 3]
    
    #The idea is to store 1 as value in a map for all numbers between 1 and
    #1000000 which have only 1,2 and 3 as digits.
    #We can then easily check for the required numbers from the map.
    mp[1]=1
    mp[2]=1
    mp[3]=1

    j=0
    
    #using a loop in which we keep multiplying the number in list with 10 and 
    #add 1,2 and 3 to it and store them in list one by one thus only numbers 
    #with 1,2 and 3 as digits are stored in the list.
    #This process continues till the number is less than or equal to 1000000.
    while(num<=1000000):
        
        #storing the number from list in num2.
        num2=a[j]
        j+=1
        
        #multiplying num2 with 10 and adding 1 and we store it in the list
        #only if it is less than or equal to 1000000.
        if((num2*10+1)<=1000000):
            a.append(num2*10+1)
            #updating the value in map.
            mp[num2*10+1]=1
            
        #multiplying num2 with 10 and adding 2 and we store it in the list
        #only if it is less than or equal to 1000000.
        if((num2*10+2)<=1000000):
            a.append(num2*10+2)
            #updating the value in map.
            mp[num2*10+2]=1
            
        #multiplying num2 with 10 and adding 3 and we store it in the list
        #only if it is less than or equal to 1000000.
        if((num2*10+3)<=1000000):
            a.append(num2*10+3)
            #updating the value in map.
            mp[num2*10+3]=1
            
        #updating num which controls the loop.
        num=num2*10+3





#{ 
 # Driver Code Starts
#Initial Template for Python 3

mp = {}

#Position this line where user code will be pasted.


if __name__ == '__main__':
    findAll()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr=[int(x) for x in input().strip().split()]
        arr.sort()
        flag = 0
        for i in range(n):
            if arr[i] in mp:
                print(arr[i], end=" ")
                flag=1
        if(flag==0):
            print(-1)
        else:
            print()

# } Driver Code Ends