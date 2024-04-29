#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        
        def freeList(node): 
            while (node != None): 
                next = node.next
                node = next
            return node 
            
        if (head == None): 
            return None
  
        if (k == 1): 
            freeList(head) 
            return None
      
        n=head
        p=None
        
        c=0
        while n:
            c+=1
            
            if (k == c):
                p.next=n.next
                
                c=0
            
            if c!=0:
                p=n
               
            n=p.next
            
        
        return head
            
            
#{ 
 # Driver Code Starts
class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)

# } Driver Code Ends