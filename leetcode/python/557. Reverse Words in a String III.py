class Solution:
    def reverseWords(self, s):
        temp = s.split()
        result = ''
        
        i=0
        while i<len(temp):
            result+=temp[i][::-1]
            if i!=len(temp)-1:
                result+=' '
            i+=1
            
        return result
        