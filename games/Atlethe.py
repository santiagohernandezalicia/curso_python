class Atlethe:
    ''' Atlethe class. whit only name atribute'''

    def __init__(self, name:str):
        self.name = name
    def __str__ (self):
        return f"atlethe: {self.name}"
    def __repr__(self):
        return f"atlethe:({self.name})"

    def display(self):
        print(f"{self.name}")        

if __name__ == "__main__":
        a =Atlethe("Ana, G")
        a.display
        print(a)
        print(repr(a))