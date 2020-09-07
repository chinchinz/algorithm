# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         res = []
#         products.sort()
#         for i in range(len(searchWord)):
#             res.append([])
#             for product in products :
#                 if product.startswith(searchWord[:i+1]):
#                     res[i].append(product)
#                     if len(res[i])==3: break
#         return res
    
##############

class Solution:
    def suggestedProducts(self, A, word):
        A.sort()
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, i)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return res