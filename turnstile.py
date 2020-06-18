
class State:

    def __init__(self, name=None, transition=None, direction=None):
        self.name = name
        self.transition = transition
        self.direction = direction


class StateMachine:

    def __init__(self, states=None, initial_state=None):
        self.state_mapping = {state.name: state for state in states}
        self.initial_state = initial_state
        self.current_state = initial_state

    def transition(self, action):
        if self.current_state.transition == action:
            self.current_state = self.state_mapping[self.current_state.direction]


