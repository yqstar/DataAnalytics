class Solution:
    def bubble_sort(self, nums_list):
        n = len(nums_list)
        for j in range(n-1):
            for i in range(n-j-1):
                if nums_list[i] > nums_list[i + 1]:
                    nums_list[i], nums_list[i + 1] = nums_list[i + 1], nums_list[i]
        return nums_list



st = Solution()

print(st.bubble_sort([1,9,5,4,10]))
