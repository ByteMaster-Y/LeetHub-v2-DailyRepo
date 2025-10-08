from bisect import bisect_left # 이진탐색 임포트
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []
        for spell in spells:
            min_potion_needed = (success + spell - 1) // spell
            k = bisect_left(potions, min_potion_needed)
            count = len(potions) - k
            answer.append(count)
        return answer