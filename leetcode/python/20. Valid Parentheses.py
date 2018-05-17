class Solution:
    def isValid(self, s):
        temp_list = []
        
        push_list = ['(','{','[']
        
        for char in s:
            if char in push_list:
                temp_list.append(char)
                continue
            elif char==')':
                if not temp_list or temp_list.pop()!='(':
                    return False
            elif char=='}':
                if not temp_list or temp_list.pop()!='{':
                    return False
            elif char==']':
                if not temp_list or temp_list.pop()!='[':
                    return False
        
        if not temp_list:
            return True
        else:
            return False