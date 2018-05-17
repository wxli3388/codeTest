class Solution:
    def hammingDistance(self, x, y):
        temp_x = ['0'] * 32
        temp_y = ['0'] * 32
        
        bin_x = bin(x)[2:]
        len_x = len(bin_x)
        bin_y = bin(y)[2:]
        len_y = len(bin_y)
        
        for index,char in enumerate(bin_x):
            temp_x[31-(len_x-index-1)] = char
        for index,char in enumerate(bin_y):
            temp_y[31-(len_y-index-1)] = char
            
        diff = 0
        for i in range(32):
            if temp_x[i]!=temp_y[i]:
                diff+=1
        return diff