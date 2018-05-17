class Solution:
    def numJewelsInStones(self, J, S):
        j_list = []
        for char in J:
            j_list.append(char)
            
        count = 0
        for char in S:
            if char in j_list:
                count+=1
        return count