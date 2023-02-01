class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        max_num = ans[0]
        for num in reversed(arr[1:]):
            if num > max_num:
                max_num = num
                ans.append(max_num)
            else:
                ans.append(max_num)
        return ans[::-1]
