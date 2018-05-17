class Solution:
    def findWords(self, words):
        l1 = ['q','w','e','r','t','y','u','i','o','p']
        l2 = ['a','s','d','f','g','h','j','k','l']
        l3 = ['z','x','c','v','b','n','m']
        result = []
        for word in words:
            temp = word.lower()
            t1 = 0
            t2 = 0
            t3 = 0
            for char in temp:
                if char in l1:
                    t1 = 1
                if char in l2:
                    t2 = 1
                if char in l3:
                    t3 = 1
                if t1+t2+t3>1:
                    break
            if t1+t2+t3==1:
                result.append(word)
        return result