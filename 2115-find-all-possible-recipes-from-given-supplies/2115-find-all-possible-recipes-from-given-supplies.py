class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(ingredients)
        supp = set(supplies)
        q = deque()
        res = []
        def canMake(j):
            t= True
            for i, ingridient in enumerate(ingredients[j]):
                if ingridient not in supp:
                    t = False
            if t:
                q.append(recipes[j])
                made.add(j)    
        made = set()
        for i in range(n):
            canMake(i)
        while q:
            nyaata  = q.popleft()
            res.append(nyaata)
            supp.add(nyaata)        
            for i in range(n):
                if i not in made: 
                    canMake(i)
        return res