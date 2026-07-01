class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      freq = {}
      for i in range(len(nums)):
        remaining = target - nums[i]

        if remaining in freq:
            return [freq[remaining], i]

        freq[nums[i]] = i
