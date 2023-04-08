class Solution:
    def createBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.createBST(nums[:mid])
        root.right = self.createBST(nums[mid+1:])
        return root
        

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.createBST(nums)
