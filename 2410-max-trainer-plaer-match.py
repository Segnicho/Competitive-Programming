class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p = len(players)
        t = len(trainers)
        i = j = 0
        cnt = 0
        while i<p and j < t:
            if players[i] <= trainers[j]:
                cnt+=1
                i+=1
                j+=1
            else:
                j+=1
        return cnt
