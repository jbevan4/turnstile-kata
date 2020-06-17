class StateMachine:

    def __init__(self, states=None, transitions=None, terminals=None, initial_state=None):
        self.states = states
        self.transitions = transitions
        self.terminals = terminals
        self.initial_state = initial_state
        self.current_state = initial_state

    def transition(self, action):
        try:
            query_index = self.states.index(self.current_state)
            if self.transitions[query_index] == action:
                self.current_state = self.states[query_index + 1]
        except Exception as e:
            print(e)
