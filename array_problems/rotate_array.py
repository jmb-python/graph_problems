'''
Given an array, rotate the array to the right by k steps, 
where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
                             [1,2,3,4,5,6,7]
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Complexity:
    Time: O(n), if k = len(array)
    Space: O(1) (ideal)

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

To use O(1) in Space complexity, use the following algorithm:
- Reverse whole array.
- Reverse first k elements
- Reverse rest n-k elements.
'''


def rotate_array(nums, k):
    # Edge case emtpy or None array
    if nums is None or len(nums) == 0:
        print("Empty or None array, won't rotate")

    # If k is bigger than the arrize size, calculate to only do one reverse.
    if k > len(nums):
        k = k % len(nums)

    reverse_array_in_place(nums, 0, len(nums))
    reverse_array_in_place(nums, 0, k)
    reverse_array_in_place(nums, k, len(nums))


# Including start, excluding end
def reverse_array_in_place(arr, start, end):
    end -= 1
    while start < end:
        aux = arr[start]
        arr[start] = arr[end]
        arr[end] = aux
        start += 1
        end -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_array(nums, k)
    for i in len(nums) - 1:
        print({nums[i]}, end=" ")
