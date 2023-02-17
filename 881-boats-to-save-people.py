class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        lptr = 0
        rptr = len(people)-1
        boatNumber = 0
        people.sort()
        print(people)
        while lptr <= rptr:
            if ((people[lptr] + people[rptr]) <= limit):
                boatNumber = boatNumber+ 1
                lptr+=1
                rptr -= 1
            elif ((people[lptr] + people[rptr]) > limit):
                boatNumber += 1
                rptr -= 1
        return boatNumber
