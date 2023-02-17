class Solution:
    def compress(self, chars: List[str]) -> int:
        space = []
        lptr,rptr = 0,0
        count = 0
        while rptr<len(chars):
            if chars[lptr]==chars[rptr]:
                rptr+=1
                count+=1
            elif chars[lptr]!=chars[rptr]:
                if count==1:
                    space.append(chars[lptr])
                else:
                    space.extend([chars[lptr]]+list(str(count)))
                lptr=rptr
                count=0
        # print(space)
        if count==1:
            space.append(chars[lptr])
        else:
            space.extend([chars[lptr]]+list(str(count)))
        chars[:]=space           
        return len(chars)
