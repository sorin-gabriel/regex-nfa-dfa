
class Transition:
    def __init__(self, s, c, d) -> object:
        self.s = s
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return f"{self.s},'{self.c}',{self.d}"
