
from Expression import *
from NFA import *


def flattenStack(es : list, ns : list, stateCounter):
    popped = None
    while True:

        if popped is None:
            if isinstance(es[-1], LiteralExpr):
                popped = es.pop()
                ns.append(LiteralNFA(stateCounter, stateCounter+1, popped.name))
                stateCounter += 2
            else:
                break

        if popped is not None:
            if len(es) == 0:
                es.append(popped)
                break

            if isinstance(es[-1], ConcatExpr):
                if isinstance(es[-1].e1, VoidExpr):
                    es[-1].e1 = popped
                    break
                elif isinstance(es[-1].e2, VoidExpr):
                    es[-1].e2 = popped
                    popped = es.pop()
                    nfa2 = ns.pop()
                    nfa1 = ns.pop()
                    ns.append(ConcatNFA(nfa1, nfa2))

            elif isinstance(es[-1], UnionExpr):
                if isinstance(es[-1].e1, VoidExpr):
                    es[-1].e1 = popped
                    break
                elif isinstance(es[-1].e2, VoidExpr):
                    es[-1].e2 = popped
                    popped = es.pop()
                    nfa2 = ns.pop()
                    nfa1 = ns.pop()
                    ns.append(UnionNFA(stateCounter, stateCounter + 1, nfa1, nfa2))
                    stateCounter += 2

            elif isinstance(es[-1], StarExpr):
                if isinstance(es[-1].e, VoidExpr):
                    es[-1].e = popped
                else:
                    popped = es.pop()
                    nfa = ns.pop()
                    ns.append(StarNFA(stateCounter, stateCounter + 1, nfa))
                    stateCounter += 2
            
            elif isinstance(es[-1], PlusExpr):
                if isinstance(es[-1].e, VoidExpr):
                    es[-1].e = popped
                else:
                    popped = es.pop()
                    nfa = ns.pop()
                    ns.append(PlusNFA(stateCounter, stateCounter + 1, nfa))
                    stateCounter += 2

    return stateCounter

def prenexParse(prenexString):
    expStack = []
    nfaStack = []
    stateCounter = 0
    for token in prenexString:
        if token == "CONCAT":
            expStack.append(ConcatExpr(VoidExpr(), VoidExpr()))
        elif token == "UNION":
            expStack.append(UnionExpr(VoidExpr(), VoidExpr()))
        elif token == "STAR":
            expStack.append(StarExpr(VoidExpr()))
        elif token == "PLUS":
            expStack.append(PlusExpr(VoidExpr()))
        else:
            expStack.append(LiteralExpr(token))
            stateCounter = flattenStack(expStack, nfaStack, stateCounter)
    return (expStack.pop(), nfaStack.pop())
