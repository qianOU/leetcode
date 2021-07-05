class Solution:
    # 小根堆
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        n1, n2 = len(nums1), len(nums2)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(n1)]
        heapq.heapify(heap)

        count = 0
        ans = []
        while count < k:
            _, i, j = heapq.heappop(heap)
            count += 1
            ans.append([nums1[i], nums2[j]])
            if j+1 < n2:
                j += 1
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))

        return ans