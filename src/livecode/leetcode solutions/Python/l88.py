nums1 = [1, 4, 9]
l = 0
nums2 = [2, 5, 8]
r = 0

res = []

i = 0
while i < len(nums1) + len(nums2):

    if nums1[l] < nums2[r]:
        i += 1
        res.append(nums1[l])
        l += 1
        print(res)
    if nums1[l] > nums2[r]:
        i += 1
        res.append(nums2[r])
        r+=1
        print(res)


#
nums1 = [1, 4, 9]
nums2 = [2, 5, 8]

i, j = 0, 0

res = []

while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j += 1


print(res)