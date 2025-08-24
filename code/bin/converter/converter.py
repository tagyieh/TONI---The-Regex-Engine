from lib import toni_classes

import sys

epsilon_closures = dict()
visited = []

symbols = [x for x in range(256)]

def get_epsilon_closures():
    '''
    For all states, get their epsilon closure
    '''

    for key,value in toni_classes.state_dictionary.items():
        global visited 
        visited = []
        epsilon_closures[value.name] = get_epsilon_closure_for_state(value)

def get_epsilon_closure_for_state(state: toni_classes.State):
    '''
    For the current state, obtain all states that can be accessed
    via empty tansitions
    '''

    epsilon_closure = [state]
    global visited
    # consider we already visited this state, to avoid circular transitions
    visited.append(state)

    if isinstance(state, toni_classes.Char_Class_State) or isinstance(state, toni_classes.Star_State):
        # If the state doesn't have an empty transition, the only state accessed is the state itself
        epsilon_closures[state.name] = epsilon_closure
        return epsilon_closure

    if state.character_code == -1:
        # If the state has an empty transition, all child states must be added
        for output_state in state.output_states:
            if output_state not in visited:
                epsilon_closure.extend(get_epsilon_closure_for_state(output_state))

    return epsilon_closure

def union_closures(to_closure: list[toni_classes.State]):
    '''
    Unite the closures. For this, take advantage of sets and their union operation '|'
    '''
    union = epsilon_closures[to_closure[0].name]

    for state in to_closure[1:]:
        current_closure = epsilon_closures[state.name]
        union = list(set(union) | set(current_closure))

    # Get the resulting name that will identify the new DFA state
    sorted_union = sorted((element.name for element in union), key=lambda name: int(name[1:]))

    return "_".join(sorted_union), union

def new_transition(current_state: toni_classes.DFA_State, new_state: toni_classes.DFA_State, current_symbol: str):
    '''
    Make a transition between two states for a given symbol
    '''
    current_state.transitions[current_symbol] = new_state

def convert_nfa_to_dfa(start_state: toni_classes.State):
    '''
    Convert from an NFA to a DFA
    '''

    # Get the epsilon closures of all states
    get_epsilon_closures()
    processed_states = dict()

    # Start at the starting state
    union = epsilon_closures[toni_classes.start_state]
    sorted_union = sorted((element.name for element in union), key=lambda name: int(name[1:]))
    first_closure_name = "_".join(sorted_union)

    dfa_is_final = toni_classes.final_state in first_closure_name
    first_dfa_state = toni_classes.DFA_State(first_closure_name, dict(), dfa_is_final)

    unprocessed_states = dict()
    unprocessed_states[first_closure_name]=(first_dfa_state,union)

    # While there are DFA states that haven't been processsed, keep going
    while unprocessed_states:
        closure_name, (value) = unprocessed_states.popitem()
        current_dfa_state, closure = value
        tmp_states = dict()
        # Iterate over all symbols
        for symbol in symbols:
            output_nfa_states = []
            # Find all states in the closure that have transitions for the current symbol
            for state in closure:
                if (
                    isinstance(state, toni_classes.Char_Class_State) 
                    and symbol in state.character_codes
                ):
                     output_nfa_states += state.output_states
                elif isinstance(state, toni_classes.State) and symbol == state.character_code:
                    output_nfa_states += state.output_states
                else:
                    pass

            # right now, output_nfa_states has the states that we can achieve with 
            # the current symbol. Therefore, we need to get the closure of each state,
            # because we can also access their sigma transitions, and union them

            # new_closure should be a string saying which states
            # are in the closure, something like q0_q3_q7.
            # the string must be sorted to be identifiable.
            # We also need to know the closure itself
            
            # If there is a state with transitions for the current symbol
            if len(output_nfa_states) > 0:
                # Make the union of the closures
                new_closure_name, new_closure = union_closures(output_nfa_states)

                # so, the new dfa state must either be created or obtained,
                # in order to use it in the transition
                new_dfa_state = None

                # If created and processed
                if new_closure_name in processed_states:
                    new_dfa_state = processed_states[new_closure_name]
                # If created but not processed yet
                elif new_closure_name in tmp_states:
                    new_dfa_state = tmp_states[new_closure_name]
                elif new_closure_name in unprocessed_states:
                    new_dfa_state,_ = unprocessed_states[new_closure_name]
                # Otherwise, create it
                else:
                    dfa_is_final = toni_classes.final_state in new_closure_name
                    new_dfa_state = toni_classes.DFA_State(new_closure_name, dict(), dfa_is_final) # THIS OVERWRITES THE SYMBOLS OF CHAR CLASS STATE
                    unprocessed_states[new_closure_name] = (new_dfa_state, new_closure)
                    tmp_states[new_closure_name] = new_dfa_state
                # Finally, make the transition to the DFA state
                new_transition(current_dfa_state, new_dfa_state, current_symbol=symbol)
            else:
                pass

        # Once we processed all strings, we can consider this state finished
        processed_states[closure_name] = current_dfa_state

    first_key = next(iter(processed_states))

    return processed_states[first_key]
