class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productArray = []
        # Check number of zeroes, if more than 1 then all products will
        # be zero
        if nums.count(0) > 1:
            for n in nums:
                productArray.append(0)
        else: 
            finalProduct = 1
            zerolessProduct = 1

            for n in nums:
                if n != 0:
                    zerolessProduct *= n
                finalProduct *=  n

            for n in nums:
                if n != 0: 
                    product = int(finalProduct/n)
                    productArray.append(product)
                else:
                    productArray.append(zerolessProduct)

        return productArray



        