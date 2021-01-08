
class ListNode:
    def __init__(self, x):
         self.data = x
         self.next = None
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Solution:
    def __init__(self):
        self.head = None

    def add(self,item):
        newNode = ListNode(item)
        if self.head==None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head=newNode
    def printlist(self):
        current = self.head
        while current:
            print(current.getData())
            current=current.getNext()


    def addTwoNumbers(self, l1, l2 ):
        sumval = 0
        root = curr = ListNode(0)
        while l1 or l2 or sumval:
            if l1:
                sumval += l1.getData()
                l1 = l1.next
            if l2:
                sumval += l2.getData();
                l2 = l2.next
            self.add(sumval % 10)
            sumval //= 10

print("first")
test = Solution()
test.add(2)
test.add(6)
test.add(4)
test.printlist()
print("---second---")
test1 = Solution()
test1.add(5)
test1.add(6)
test1.add(4)
test1.printlist()
print("----Now sum----")
sum = Solution()
sum.addTwoNumbers(test.head,test1.head)
sum.printlist()
