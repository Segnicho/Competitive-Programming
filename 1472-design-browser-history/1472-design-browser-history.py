class SiteNode:
    def __init__(self, url = "", before=None, next=None):
        self.url = url
        self.next = next
        self.before = before
class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = SiteNode(url=homepage)
    def visit(self, url: str) -> None:
        newSite = SiteNode(url=url,before=self.homepage)
        self.homepage.next=newSite
        self.homepage=self.homepage.next

    def back(self, steps: int) -> str:
        i = 0
        while self.homepage and self.homepage.before:
            if i == steps:
                break
            self.homepage= self.homepage.before
            i+=1
        return self.homepage.url if self.homepage else None
    def forward(self, steps: int) -> str:
        i = 0
        while self.homepage.next:
            if i == steps:
                break
            self.homepage= self.homepage.next
            i+=1
        return self.homepage.url if self.homepage else None
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

