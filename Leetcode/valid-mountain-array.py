class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = None
        n = len(arr)
        if n < 3:
            return False
        for i in range(1, n):
            if up:
                if arr[i] < arr[i-1]:
                    up = False
                elif arr[i] == arr[i-1]:
                    return False
            elif up is None:
                if arr[i] > arr[i-1]:
                    up = True
                else:
                    return False
            else:
                if arr[i] >= arr[i-1]:
                    return False
        if up:
            return False
        return True
