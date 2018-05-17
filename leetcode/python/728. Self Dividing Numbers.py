class Solution:
    def selfDividingNumbers(self, left, right):
        match_list = []
        
        for i in range(left,right+1):
            isDivide = True
            for j in str(i):
                if int(j)==0:
                    isDivide = False
                    break
                if i%int(j)!=0:
                    isDivide = False
                    break
            if isDivide==True:
                match_list.append(i)
        return match_list