class Comment:

    def __init__(self,author,id_movie,text) -> None:
        self.author = author
        self.id_movie = id_movie
        self.text = text
    
    def get(self):
        return (self.author,self.text,self.id_movie)