class Solution:
    def uniqueMorseRepresentations(self, words):
        
        trans_list = []
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            s = ''
            for char in word:
                s+=morse[ord(char)-97]
            if s not in trans_list:
                trans_list.append(s)
                
        return len(trans_list)