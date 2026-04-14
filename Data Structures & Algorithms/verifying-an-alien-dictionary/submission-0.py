class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # if word A is prefix of word B, word B must be After word A
        # first differing char

        orderIndx = {}
        for i,c in enumerate(order):
            orderIndx[c] = i

        for i in range(len(words)-1):
            W1,W2 = words[i],words[i+1]

            for j in range(len(W1)):
                if j == len(W2):
                    return False

                if W1[j] != W2[j]:
                    if orderIndx[W2[j]] < orderIndx[W1[j]]:
                        return False
                    break
        return True

        