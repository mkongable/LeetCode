class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        """
        create a stack
        while we aren't at the end of the push list:
            if the current element in push list is not the current element in the popped list, push the current push_list item onto the stack
            else:
                while current pop list item is the same as stack top:
                    pop and advance the pop list
        if stack is not empty, return false
        else return true
        """
        stack = []
        popIdx = 0
        for push_item in pushed:
            stack.append(push_item)
            while stack and popped[popIdx] == stack[-1]:
                stack.pop()
                popIdx += 1
        return False if stack else True
        

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(Solution().validateStackSequences(pushed, popped))