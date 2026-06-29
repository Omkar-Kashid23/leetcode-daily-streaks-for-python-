class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(t in word for t in patterns)