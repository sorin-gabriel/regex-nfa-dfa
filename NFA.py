
from State import *
from Transition import *

epsilon = "ε"

class NFA:

    def epsilonClosure(self, state : State):
        closure = []
        neighbors = [state]

        while len(neighbors) > 0:
            s = neighbors.pop()
            if s not in closure:
                closure.append(s)

            for t in self.transitions:
                if s == t.s and t.c == epsilon and t.d not in closure and t.d not in neighbors:
                    neighbors.append(t.d)
        return closure

    def NFAtoDFA(self):
        self.alphabet.sort()
        dfa_alphabet = self.alphabet
        dfa_initial = 0
        dfa_state_counter = dfa_initial
        dfa_final = []
        dfa_sink = -1
        dfa_transitions = []
        nfa_indexed_groups = []

        neighbors = [self.epsilonClosure(self.initial)]

        while len(neighbors) > 0:
            nfa_group = neighbors.pop()
            if nfa_group not in nfa_indexed_groups:
                nfa_indexed_groups.append(nfa_group)
                dfa_state_counter += 1

            for symbol in dfa_alphabet:
                symbol_succ = []
                for nfa_state in nfa_group:
                    for t in self.transitions:
                        if symbol == t.c and nfa_state == t.s and t.d not in symbol_succ:
                            symbol_succ.append(t.d)

                if len(symbol_succ) > 0:
                    group_succ = []
                    for state in symbol_succ:
                        closure = self.epsilonClosure(state)
                        for nfa_state in closure:
                            if nfa_state not in group_succ:
                                group_succ.append(nfa_state)

                    if len(group_succ) > 0:
                        if group_succ not in neighbors and group_succ not in nfa_indexed_groups:
                            neighbors.append(group_succ)
                        if group_succ not in nfa_indexed_groups:
                            nfa_indexed_groups.append(group_succ)
                            dfa_state_counter += 1
                        dfa_transitions.append(Transition(nfa_indexed_groups.index(nfa_group), symbol, nfa_indexed_groups.index(group_succ)))
                else:
                    dfa_transitions.append(Transition(nfa_indexed_groups.index(nfa_group), symbol, dfa_sink))
                

        for symbol in dfa_alphabet:
            dfa_transitions.append(Transition(dfa_sink, symbol, dfa_sink))
        
        for group in nfa_indexed_groups:
            for state in group:
                if state == self.final and nfa_indexed_groups.index(group) not in dfa_final:
                    dfa_final.append(nfa_indexed_groups.index(group))
        dfa_final.sort(reverse=True)

        for t in dfa_transitions:
            if t.s == -1:
                t.s = dfa_state_counter
            if t.d == -1:
                t.d = dfa_state_counter
        dfa_state_counter += 1

        str_alphabet = ''.join(str(s) for s in dfa_alphabet)
        str_final = ' '.join(str(s) for s in dfa_final)
        str_delta = '\n'.join(str(s) for s in dfa_transitions)

        return '\n'.join(str(s) for s in [
            "Alphabet: " + str_alphabet,
            "Number of states: " + str(dfa_state_counter),
            "Initial state: " + str(dfa_initial),
            "Final states: " + str_final,
            "Transition table (source, symbol, destination):",
            str_delta
            ])

    def __init__(self, a, s, i, f, t) -> object:
        self.alphabet = list(set(a))
        self.states = s
        self.initial = i
        self.final = f
        self.transitions = t

class VoidNFA(NFA):
    def __init__(self) -> NFA:
        pass

class LiteralNFA(NFA):
    def __init__(self, i, f, l) -> NFA:
        states = [Normal(i), Normal(f)]
        transitions = [Transition(Normal(i), str(l), Normal(f))]
        super().__init__([l], states, Normal(i), Normal(f), transitions)

class ConcatNFA(NFA):
    def __init__(self, nfa1, nfa2) -> NFA:
        alphabet = nfa1.alphabet + nfa2.alphabet
        states = nfa1.states + nfa2.states
        transitions = nfa1.transitions + nfa2.transitions
        transitions += [Transition(nfa1.final, str(epsilon), nfa2.initial)]
        super().__init__(alphabet, states, nfa1.initial, nfa2.final, transitions)

class UnionNFA(NFA):
    def __init__(self, i, f, nfa1, nfa2) -> NFA:
        alphabet = nfa1.alphabet + nfa2.alphabet
        states = nfa1.states + nfa2.states + [Normal(i), Normal(f)]
        transitions = nfa1.transitions + nfa2.transitions
        transitions += [
            Transition(Normal(i), str(epsilon), nfa1.initial),
            Transition(Normal(i), str(epsilon), nfa2.initial),
            Transition(nfa1.final, str(epsilon), Normal(f)),
            Transition(nfa2.final, str(epsilon), Normal(f))
        ]
        super().__init__(alphabet, states, Normal(i), Normal(f), transitions)

class StarNFA(NFA):
    def __init__(self, i, f, nfa) -> NFA:
        states = nfa.states + [Normal(i), Normal(f)]
        transitions = nfa.transitions
        transitions += [
            Transition(Normal(i), str(epsilon), nfa.initial),
            Transition(Normal(i), str(epsilon), Normal(f)),
            Transition(nfa.final, str(epsilon), Normal(f)),
            Transition(nfa.final, str(epsilon), nfa.initial),
        ]
        super().__init__(nfa.alphabet, states, Normal(i), Normal(f), transitions)

class PlusNFA(NFA):
    def __init__(self, i, f, nfa) -> NFA:
        states = nfa.states + [Normal(i), Normal(f)]
        transitions = nfa.transitions
        transitions += [
            Transition(Normal(i), str(epsilon), nfa.initial),
            Transition(nfa.final, str(epsilon), Normal(f)),
            Transition(nfa.final, str(epsilon), nfa.initial),
        ]
        super().__init__(nfa.alphabet, states, Normal(i), Normal(f), transitions)
