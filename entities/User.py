import hashlib

class User:
    name:str
    password:str

    def __init__(self,name,password):
        self.name = name
        self.password = hashlib.blake2b(password.encode()).hexdigest()

    def get(self):
        return self.name,self.password
