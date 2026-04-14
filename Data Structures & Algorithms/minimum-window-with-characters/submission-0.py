class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" :
            return ""
        countT , windowT = {} , {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        l=0
        have , need = 0 , len(countT)
        res, reslen = [-1,-1] , float("infinity")
        for r in range(len(s)):
            c = s[r]
            windowT[c] = 1 + windowT.get(c,0)

            if c in countT and windowT[c] == countT[c]:
                have+=1
            while have == need:
                #update the result 
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = r-l+1
                # now pop from left - window shift (one by one) 
                windowT[s[l]] -=1
                if s[l] in countT and windowT[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""
        