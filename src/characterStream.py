class CharacterStream:
    def __init__(self, string:str):
        self.string = string
        self.index = 0
        self.eof = string == ""
    
    def get_next(self):
        if self.eof:
            raise EOFError

        char = self.string[self.index]
        self.index += 1

        if self.index == len(self.string):
            self.eof = 1

        return char

    def unread(self):
        self.index -= 1
        self.eof = False