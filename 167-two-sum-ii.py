class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers)-1
        while front < back:
            if numbers[front] + numbers[back] == target :
                return [front+1, back+1]
            elif numbers[front] + numbers[back] < target:
                front = front +1
            else: 
                back = back-1
                
