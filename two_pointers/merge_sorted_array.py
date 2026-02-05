class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # this is the last index of nums1
        last = m + n - 1
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1
                print("Where m>n")
                print("nums1:",nums1)
                print("nums2:", nums2)
                print("n:", n)
                print("m:",m)
            else:
                nums1[last] = nums2[n-1]
                n -=1
                print("where n>=m")
                print("nums1:",nums1)
                print("nums2:", nums2)
                print("n:", n)
                print("m:",m)
            last -=1
        
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1
