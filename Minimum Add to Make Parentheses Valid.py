class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = "((("

        stack = []

        counter = 0


        moves = 0
        while counter < len(s):
            
            if s[counter] == ")" and not stack:
                moves += 1
            
            elif s[counter] == ")" and stack[len(stack) - 1] == "(":
                stack.pop()
                
            elif s[counter] == "(":
                stack.append("(")
                
            counter += 1
                
        moves += (len(stack))

        return moves
        # print ("moves is ", moves)
