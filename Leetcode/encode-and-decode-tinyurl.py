from uuid import uuid4

class Codec:

    def __init__(self):
        self.urls = {}
        self.baseURL = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url_ID = uuid4().hex
        encoded_url = self.baseURL + url_ID
        self.urls[encoded_url] = longUrl
        return encoded_url

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
