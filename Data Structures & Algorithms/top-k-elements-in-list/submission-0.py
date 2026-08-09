class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
    
        newList = []

        for i in range(k):
            greatest = 0
            greatestKey = None
            for key, value in count.items():
                if(value > greatest):
                    greatest = value
                    greatestKey = key
            newList.append(greatestKey)
            count.pop(greatestKey)

        return(newList)
        