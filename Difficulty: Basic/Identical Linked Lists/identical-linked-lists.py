# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    
    current1 = head1
    current2 = head2
    while current1 !=None and current2!=None:
        if(current1.data != current2.data):
            return False
        current1=current1.next
        current2 = current2.next

    return (current1 ==None and current2==None)
            
        
            
    
    
    
    
    
    # while n:
    #     c+=1
    #     n=n.next
    # while m:
    #     l+=1
    #     m=m.next
    
   
        
    # if c!=l:
    #     return False

    # if c==l:
    #     while m and n:
    #         if m.data != n.data:
    #             return False
    #         else:
    #             c-=1
    #             l-=1
    #         n=n.next
    #         m=m.next
    #     if c==0 and l==0:
    #         return True
    # else:
    #     return True
    

    
    # if c==l:
    #     return True
    # else:
    #     return False
        


#{ 
 # Driver Code Starts
# Node Class
class node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if (areIdentical(head1, head2)):
            print('true')
        else:
            print('false')

# } Driver Code Ends