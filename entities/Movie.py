class Movie:
    title: str
    url: str
    text: str

    def __init__(self,title,url,text):
        self.title = title
        self.url = url
        self.text = text

    def get(self):
        return (self.title,self.url,self.text)
