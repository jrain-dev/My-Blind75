class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Used to store values
        CheckList = []

        for item in nums:
            if item not in CheckList:
                CheckList.append(item)
        
        counter = len(CheckList)

        for item in nums:
            if item in CheckList:
                counter = counter - 1
        
        if counter == 0:
            return False
        else:
            return True

    def removeDuplicates(self, nums: List[int]) -> int:
        
        newList = []

        for i in nums[:]:
            if i not in newList:
                newList.append(i)
            elif i in newList:
                nums.remove(i)
                
        k = len(nums)

        return k

    def isAnagram(self, s: str, t: str) -> bool:

        word1 = list(s)
        word2 = list(t)

        letterIsPresent = True

        if len(word1) != len(word2):
                return False

        for letter in word1:
            if letter in word2:
                word2.remove(letter)   
            else:
                letterIsPresent = False
                break
            

        return letterIsPresent

    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in nums[:]:
            if i == val:
                nums.remove(i)
            
        k = len(nums)

        return k

    def getConcatenation(self, nums: List[int]) -> List[int]:
    
        ans = []
        mult = range(2)

        for i in mult:
            for i in nums:
                ans.append(i)
        
        return ans

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        newList = []
        revList = [] 
        
        while head:
            newList.append(head.val)
            head = head.next
        
        for n in newList[:]:
            revList.append(newList[-1])
            newList.pop()

        #THIS ONE RIGHT HERE
        head = ListNode(revList[0])
        
        current = head

        for n in revList[1:]:
            current.next = ListNode(n)
            current = current.next

        return head
