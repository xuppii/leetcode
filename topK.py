# my_list = [1, 2, 3, 2, 1, 1, 4, 5, 4, 4]
# #my_array = list([0] * 6)
# #counter_list[len(my_list)] = {0}
# #my_array = [0 for _ in range(len(my_list))]
# counts = {}
# for item in my_list:
#     if item in counts:
#         counts[item] += 1
#     else:
#         counts[item] = 1
# max = 0
# save_item = 0
# for item, count in counts.items():
#     print(f"{count} and {max}")
#     if count > max:
#         max = count
#         save_item = item
# print(f"{save_item}: {max}")
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res