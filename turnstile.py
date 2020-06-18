class State:

    def __init__(self, name=None, transitions=None):
        self.name = name
        self.transitions = {k: v for k, v in transitions}


class StateMachine:

    def __init__(self, states=None, initial_state=None):
        self.state_mapping = {state.name: state for state in states}
        self.initial_state = initial_state
        self.current_state = initial_state

    def transition(self, action):
        if self.current_state.transitions.get(action):
            self.current_state = self.state_mapping[self.current_state.transitions.get(action)]


