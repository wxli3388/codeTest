class Solution:
    def flipAndInvertImage(self, A):
        
        for list_index,l in enumerate(A):
            l = l[::-1]
            for index,value in enumerate(l):
                l[index] = 1 - value
            A[list_index]=l
        return A