class Solution:
    def romanToInt(self, s):
        sum = 0
        i=0
        dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        while i<len(s):
            if i+1<len(s) and dict[s[i+1]]>dict[s[i]]:
                sum += dict[s[i+1]] - dict[s[i]]
                i+=2
            else:
                sum += dict[s[i]]
                i+=1
                
        return sum