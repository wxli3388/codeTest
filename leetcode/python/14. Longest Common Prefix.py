class Solution:
    def longestCommonPrefix(self, strs):
        
        if strs==[]:
            return ""
        
        prefix=strs[0]
        
        for i in range(1,len(strs)):
            if strs[i]=="":
                return ""
            len1 = len(prefix)
            len2 = len(strs[i])
            
            if len2>len1:
                compareLen = len1
            else:
                compareLen = len2
            
            for index in range(compareLen):
                if strs[i][index]!=prefix[index]:
                    prefix=prefix[:index]
                    break
                if index==(compareLen-1):
                    prefix=prefix[:index+1]
        return prefix