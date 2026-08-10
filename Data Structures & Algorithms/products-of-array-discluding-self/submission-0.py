class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if i != j:
                    result *= nums[j]
            product.append(result)
        
        return product
        