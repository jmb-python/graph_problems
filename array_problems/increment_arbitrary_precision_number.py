'''
Write a program which takes as input an array of digits encoding a decimal number
D and updates the array to represent the number D + 1. For example, if the input
is (1,2,9) then you should update the array to (1,3,0). Your algorithm should work
even if it isimplemented in a language that hasfinite-precision arithmetic.

Complexity:
    Time: O(n)
    Space: O(1)

More examples, or cases, to illustrate:

Simple scenarios, simple additions to only one digit O(1) cases
4567 + 1 
4568

0000 + 2
0002

9999 + 3
10002 (carries to left the shift to 0 on all numbers except last - also, increases size of the array - if allowed, can use list or arraylist, if not
have to copy numbers - array deep copy)

2199 + 2
2201 (carries to left the shift to 0 on all numbers except last)

'''

def increment_number(nums):
    last_index = len(nums) - 1
    last_processed = last_index

    # Loop elements in array, starting from the back, and replace the 10s with addition result
    for i in range(last_index, -1, -1):
        last_processed = i
        nums[i] = nums[i] + 1
        if nums[i] == 10:
            nums[i] = 0
        else:
            break

    if nums[last_processed] == 0:
        nums.insert(0, 1)

if __name__ == "__main__":
    nums = [1,9,9]
    print(f"Original number in shape of array? {nums}")
    increment_number(nums)
    print(f"added 1, addition result: {nums}")