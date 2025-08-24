from lib import toni_classes

def traverse_NFA(start_state: toni_classes.State, regex: str) -> bool:
    '''
    Visit the first state and determine if the input string is accepted
    '''

    validRegex = visit_state(start_state,regex,0)

    if validRegex:
        return True
    else:
        return False

def finditer_NFA(start_state: toni_classes.State, target: str) -> int:
    '''
    Find number of instances the regex fits into the target string
    '''
    n = 0
    k = 0
    while (n!=-1):
        # Try to find a path
        n = finditer_aux_NFA(start_state, target, n)
        # If none is found, exit (this is the exponential nature
        # of NFA). If one was found, try starting on the next index
        k+= 1 if n!=-1 else 0
    return k

def finditer_aux_NFA(state: toni_classes.State, regex: str, index: int):
    '''
    Auxiliary function to find matches in the target string
    '''

    # If the state is final, return
    if state.isFinal:
        return index
    
    if isinstance(state,toni_classes.Star_State):
        # Go over star states if possible
        if len(regex) > index:
            index += 1
            return finditer_aux_NFA(state.output_states[0], regex, index)
        else:
            return -1

    if isinstance(state,toni_classes.Char_Class_State):
        if len(regex) <= index:
            return -1
        # Try to transition on the allowed symbol
        symbol = ord(regex[index]) if type(regex[index])!=int else regex[index]
        if symbol in state.character_codes:
            index += 1
            return finditer_aux_NFA(state.output_states[0], regex, index)
        else:
            return -1

    if state.character_code == -1:
        # If empty transtion, try any path
        for output_state in state.output_states:
            result = finditer_aux_NFA(output_state, regex, index)
            if result!=-1:
                return result

        return -1
    else:
        if len(regex) <= index:
            return -1
        # Otherwise, make the only possible transition if possible
        symbol = ord(regex[index]) if type(regex[index])!=int else regex[index]
        if len(regex) > index and state.character_code == symbol:
            index += 1
            return finditer_aux_NFA(state.output_states[0], regex, index)
        else:
            return -1

def visit_state(state: toni_classes.State, regex: str, index: int) -> bool:
    '''
    Visit NFA state and try to transition. If many paths are possible,
    choose the first one
    '''

    # If the regex is done procesing and all input was consumed, terminate
    if state.isFinal and len(regex) == index:
        return True

    if isinstance(state,toni_classes.Star_State):
        if len(regex) > index:
            index += 1
            # Transition on star state if possible
            return visit_state(state.output_states[0], regex, index)
        else:
            return False

    if isinstance(state,toni_classes.Char_Class_State):
        # Try to transition on any allowed symbol, if possible
        if len(regex) > index and ord(regex[index]) in state.character_codes:
            index += 1
            return visit_state(state.output_states[0], regex, index)
        else:
            return False

    if state.character_code == -1:
        # If empty transition, try all ppossible states until one returns a corect path
        for output_state in state.output_states:
            result = visit_state(output_state, regex, index)
            if result:
                return result

        return False
    else:
        # Otherwise, check if we can transition on the only symbol
        if len(regex) > index and state.character_code == ord(regex[index]):
            index += 1
            return visit_state(state.output_states[0], regex, index)
        else:
            return False

def traverse_DFA(start_state: toni_classes.DFA_State, regex: str) -> bool:
    '''
    Try the traversal starting on the first state and decide if the
    string can be accepted
    '''
    validRegex = visit_state_DFA(start_state, regex, 0)
    
    if validRegex:
        return True
    else:
        return False

def visit_state_DFA(start_state: toni_classes.DFA_State, regex: str, start_index: str) -> bool:
    '''
    Visit current state and try to transition. The function is not recursive, but linear
    because the DFA either finds the correct path right awat or there is no such path
    '''

    state = start_state
    index = start_index
    while (True):
        # If string is all processed and regex is in a final state, accept
        if state.isFinal and len(regex) == index:
            return True

        # Otherwise, check if we can transition on the current symbol
        if len(regex) > index and state.transitions.get(ord(regex[index])):
            state = state.transitions.get(ord(regex[index]))
            index = index + 1
            if state == None or index > len(regex):
                return False
        else:
            return False

def finditer_DFA(start_state: toni_classes.State, target: str) -> int:
    '''
    Find how many times the regex fits into the target string using DFA
    '''

    n = 0
    k = []
    s = len(target)
    while (n<s):
        # Start on the first index and keep trying linearly,
        # moving over the next possible index
        (val,n) = finditer_aux_DFA(start_state, target, n)
        n+=1
        k.append(1) if val else 0
    return k

def finditer_aux_DFA(state: toni_classes.State, regex: str, index: int):
    '''
    Auxiliary function to check if the regex matches any part of the string
    '''

    # If a final state is achieved, we accept it
    if state.isFinal:
        return (True,index)

    # String was fully processed and no path was found
    if len(regex) <= index:
        return (False,index)

    symbol = ord(regex[index]) if type(regex[index])!=int else regex[index]
    # Try to transition on the current symboil
    if len(regex) > index and state.transitions.get(symbol):
        next_state = state.transitions.get(symbol)
        new_index = index + 1
        if next_state == None:
            return (False,index)
        else:
            return finditer_aux_DFA(next_state, regex, new_index)
    else:
        return (False,index)

