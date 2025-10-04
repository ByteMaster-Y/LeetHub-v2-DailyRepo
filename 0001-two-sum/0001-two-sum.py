class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,2,3] 인 경우 fail
        # for i in range(len(nums)-1):
        #     if nums[i] + nums[i+1] == target:
        #         return i, i+1

        # for문을 두 번 돌리는 방법
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                