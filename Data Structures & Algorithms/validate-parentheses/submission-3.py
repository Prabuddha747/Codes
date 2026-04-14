class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        parenthesedict = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for bracket in s:
            if bracket in parenthesedict: # } ,),] - these are brackets - dict values
                if stack and stack[-1]==parenthesedict[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket) # appending [,(,{ - key values
        if not stack :
            return True
        else:
            return False 
        