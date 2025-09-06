class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True

        # Alternative similar Solution 2

        clean_string = self.remove_non_alphanumeric(s)
        n = len(clean_string)

        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            left += 1
            right -= 1

        return True

    def remove_non_alphanumeric(self, text):
        # Removes non alphanumeric characters and whitespace, as well as converting the string to lowercase
        # in : text = string
        # out: cleaned string

        cleaned_string = ""
        for char in text:
            if char.isalnum():
                cleaned_string += char.lower()
        return cleaned_string
