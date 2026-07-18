class Solution:
    def isValid(self, s: str) -> bool:
        bracket={')':'(','}':'{',']':'['}
        stack=[]

        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket:
                if not stack or stack.pop() !=bracket[i]:
                    return False
        return len(stack)==0





