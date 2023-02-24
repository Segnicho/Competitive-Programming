class Solution:
    def simplifyPath(self, path: str) -> str:
        parr = path.split("/")
        res = []
        for par in parr:
            if res and par == "..":
                res.pop()
            elif par == ".":
                continue
            elif par and par != "..":
                res.append(par)
        return "/"+"/".join(res)