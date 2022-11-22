
class State:
    def __init__(self, id) -> object:
        self.id = id

    def __eq__(self, o: object) -> bool:
        if isinstance(o, State):
            return self.id == o.id
        return False

    def __str__(self) -> str:
        return "S(" + str(self.id) + ")"

    def __hash__(self) -> int:
        return hash(repr(self))

class Sink(State):
    def __init__(self, id) -> State:
        super().__init__(id)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __hash__(self) -> int:
        return super().__hash__()

class Final(State):
    def __init__(self, id) -> State:
        super().__init__(id)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __hash__(self) -> int:
        return super().__hash__()

class Normal(State):
    def __init__(self, id) -> State:
        super().__init__(id)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __hash__(self) -> int:
        return super().__hash__()
