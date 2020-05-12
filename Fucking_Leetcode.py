class Solution:
    def bubble_sort(self, nums_list):
        n = len(nums_list)
        for j in range(n - 1):
            for i in range(n - j - 1):
                if nums_list[i] > nums_list[i + 1]:
                    nums_list[i], nums_list[i + 1] = nums_list[i + 1], nums_list[i]
        return nums_list

    def selection_sort(self, nums_list):
        n = len(nums_list)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n - 1):
                if nums_list[j] < nums_list[min_idx]:
                    min_idx = j
            nums_list[i], nums_list[min_idx] = nums_list[min_idx], nums_list[i]
        return nums_list


st = Solution()

print(st.bubble_sort([1, 9, 5, 4, 10]))
print(st.selection_sort([1, 9, 5, 4, 10]))

class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, item):
        """进队列"""
        self.items.insert(0,item)
 
    def dequeue(self):
        """出队列"""
        return self.items.pop()
 
    def size(self):
        """返回大小"""
        return len(self.items)
