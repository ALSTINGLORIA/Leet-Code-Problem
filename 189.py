class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        updated_k = k % len(nums)
        nums1 = nums[len(nums)-updated_k:]
        nums2 = nums[0:len(nums)-updated_k]
        nums1.extend(nums2)
        nums[:] = nums1
