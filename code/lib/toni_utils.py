from .toni_classes import State,Char_Class_State,Partial_NFA
import copy

def fix_dangling(nfa: Partial_NFA, my_state: State | Char_Class_State):
    '''
    Auxiliar method to fix dangling states, making them point to a new state
    '''
    for dangling in nfa.dangling_states:
        dangling.output_states.append(my_state)
    nfa.dangling_states = []
