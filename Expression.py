
exprDict = {
    "CONCAT" : "•",
    "UNION" : "∪",
    "STAR" : "*",
    "PLUS" : "+"
}

class Expr:
    def __init__(self) -> object:
        pass

    def __str__(self) -> str:
        return "?"

class VoidExpr(Expr):
    def __init__(self) -> Expr:
        pass

    def __str__(self) -> str:
        return "Void"

class UnaryExpr(Expr):
    def __init__(self) -> Expr:
        pass

    def __str__(self) -> str:
        return "?"

class BinaryExpr(Expr):
    def __init__(self, e1: Expr, e2: Expr, op: str) -> Expr:
        super().__init__()
        self.e1 = e1
        self.e2 = e2
        self.op = op

    def __str__(self) -> str:
        return self.e1.__str__() + " " + self.op + " " + self.e2.__str__()

class LiteralExpr(Expr):
    def __init__(self, name: str) -> Expr:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

class ConcatExpr(BinaryExpr):
    def __init__(self, e1: Expr, e2: Expr) -> BinaryExpr:
        super().__init__(e1, e2, exprDict["CONCAT"])

    def __str__(self) -> str:
        return "(" + super().__str__() + ")"

class UnionExpr(BinaryExpr):
    def __init__(self, e1: Expr, e2: Expr) -> BinaryExpr:
        super().__init__(e1, e2, exprDict["UNION"])

    def __str__(self) -> str:
        return "(" + super().__str__() + ")"

class StarExpr(UnaryExpr):
    def __init__(self, e: Expr) -> UnaryExpr:
        super().__init__()
        self.e = e

    def __str__(self) -> str:
        return self.e.__str__() + exprDict["STAR"]

class PlusExpr(UnaryExpr):
    def __init__(self, e: Expr) -> UnaryExpr:
        super().__init__()
        self.e = e

    def __str__(self) -> str:
        return self.e.__str__() + exprDict["PLUS"]
