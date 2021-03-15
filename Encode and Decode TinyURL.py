import random
class Codec:
    def __init__(self):
        self.db = {}
        
        self.prefix ="http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        aux = longUrl.split('/')
        coded = str(len(aux))
        
        for s in aux:
            if len(s) > 0:
                coded += s[0]
        while coded in self.db:
            rund = chr(random.randint(65,90))
            coded += rund
        self.db[coded] = longUrl
        
        return self.prefix + coded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        k = shortUrl.split('/')[-1]
        if k in self.db:
            return self.db[k]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
