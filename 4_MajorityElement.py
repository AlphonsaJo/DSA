class Solution(object):
    def majorityElement(self, nums):
        unique_elements = []
        counts = []

        for num in nums:
            found = False
            for i in range(len(unique_elements)):
                if unique_elements[i] == num:
                    counts[i] += 1
                    found = True
                    break

            if not found:
                unique_elements.append(num)
                counts.append(1)

        # Find the index of the element with the maximum count
        majority_index = counts.index(max(counts))
        # Retrieve the corresponding element from unique_elements
        majority_element = unique_elements[majority_index]x]

        return majority_element
