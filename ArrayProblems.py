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
