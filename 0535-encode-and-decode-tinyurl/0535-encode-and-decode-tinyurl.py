class Codec:
    def __init__(self):
        self.i = 0
        self.enc =defaultdict()
        self.dec =defaultdict()
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = longUrl.split("/")
        url.pop()
        url.append(str(self.i))
        self.i+=1
        shorter = "".join(url)
        self.enc[longUrl] = shorter
        self.dec[shorter] = longUrl
        return self.enc[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dec[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))