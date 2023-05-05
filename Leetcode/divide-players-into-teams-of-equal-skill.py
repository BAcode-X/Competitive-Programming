class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        left, right = 0, n - 1
        prev = skill[left] + skill[right]
        prod = skill[left] * skill[right]
        left += 1
        right -= 1
        while left < right:
            if skill[left] + skill[right] != prev:
                prod = -1
                break
            else:
                prod += skill[left] * skill[right]
            left += 1
            right -= 1
        return prod
