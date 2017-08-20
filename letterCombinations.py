class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Using Queue
        if len(digits) == 0:
            return []
        digit_char_map = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        letter_combinations = [""]
        for i in range(len(digits)):
            current_digit = int(digits[i])
            while len(letter_combinations[0]) == i:
                prev_char = letter_combinations.pop(0)
                for char in digit_char_map[current_digit]:
                    letter_combinations.append(prev_char+char)
        return letter_combinations
