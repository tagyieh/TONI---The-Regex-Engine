from dataclasses import dataclass, field
import copy

state_counter = 0
state_dictionary = {}
final_state = None
start_state = None

@dataclass
class State:
    """
    Represents a state that either represents a transition in one token or an empty
    transition.
    """

    character_code: int # -1 is an empty transition
    output_states: list
    isFinal: bool
    name: str

    def __init__(self, character_code, output_states, isFinal, isStart= False):
        self.character_code = character_code
        self.output_states = output_states
        self.isFinal = isFinal
        global state_counter
        self.name = "q"+str(state_counter)
        state_counter += 1

        global state_dictionary
        state_dictionary[self.name] = self

        if isFinal:
            global final_state
            final_state = self.name
        if isStart:
            global start_state
            start_state = self.name

    def __deepcopy__(self, memo):
        copied = type(self)(
            character_code=self.character_code,
            output_states=copy.deepcopy(self.output_states, memo),
            isFinal=self.isFinal
        )
        global state_counter
        copied.name="q" + str(state_counter)
        memo[id(self)] = copied
        state_counter+=1
        global state_dictionary
        state_dictionary[copied.name] = copied

        return copied

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.name == other.name

@dataclass
class Star_State:
    """
    Represents a state that make a transition in any symbol.
    """

    output_states: list[State]
    isFinal: bool
    character_codes = list(range(256))

    def __init__(self, output_states, isFinal):
        self.output_states = output_states
        self.isFinal = isFinal
        global state_counter
        self.name = "q"+str(state_counter)
        state_counter += 1
        global state_dictionary
        state_dictionary[self.name] = self

    def __deepcopy__(self, memo):
        copied = type(self)(
            character_codes=self.character_codes,
            output_states=copy.deepcopy(self.output_states, memo),
            isFinal=self.isFinal
        )
        global state_counter
        copied.name="q" + str(state_counter)
        memo[id(self)] = copied
        state_counter+=1
        global state_dictionary
        state_dictionary[copied.name] = copied

        return copied

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Star_State):
            return NotImplemented
        return self.name == other.name

@dataclass
class Char_Class_State:
    """
    Represents a state which can make a transition if any of the allowed symbols is
    matched.
    """

    character_codes: list[int]
    output_states: list[State]
    isFinal: bool

    def __init__(self, character_codes, output_states, isFinal):
        self.character_codes = character_codes
        self.output_states = output_states
        self.isFinal = isFinal
        global state_counter
        self.name = "q"+str(state_counter)
        state_counter += 1
        global state_dictionary
        state_dictionary[self.name] = self

    def __deepcopy__(self, memo):
        copied = type(self)(
            character_codes=copy.deepcopy(self.character_codes),
            output_states=copy.deepcopy(self.output_states, memo),
            isFinal=self.isFinal
        )
        global state_counter
        copied.name="q" + str(state_counter)
        memo[id(self)] = copied
        state_counter+=1
        global state_dictionary
        state_dictionary[copied.name] = copied

        return copied

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Char_Class_State):
            return NotImplemented
        return self.name == other.name

@dataclass
class Partial_NFA:
    """
    Represents an NFA with a starting state, but with dangling transitions.
    """

    start: State
    dangling_states: list[State]

@dataclass
class DFA:
    """
    TBD
    """
pass

@dataclass
class DFA_State:
    """
    
    """
    name: str
    transitions: dict # "character_code":State
    isFinal: bool
